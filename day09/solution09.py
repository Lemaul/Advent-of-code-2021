
def get_in(file):
  with open(file) as f:
    mp = f.read().split()
    for i, row in enumerate(mp):
      mp[i] = list(map(int, list(row)))
    return mp


def in_board(x, y, len_x, len_y):
  return x < len_x and y < len_y and x >= 0 and y >= 0


def find_low_points(mp):
  steps = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
  ]

  res = 0
  for i in range(len(mp)):
    for j in range(len(mp[0])):
      possible = 0
      bigger = 0
      for step in steps:
        x = i + step[1]
        y = j + step[0]
        if in_board(x, y, len(mp), len(mp[0])):
          possible += 1
          if mp[i][j] < mp[x][y]:
            bigger += 1
      if bigger == possible:
        res += mp[i][j] + 1
  
  return res


def count_size(mp, visited, x, y, basin):
  visited[x][y] = 1
  steps = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
  ]

  for step in steps:
    newx = x + step[1]
    newy = y + step[0]
    if in_board(newx, newy, len(mp), len(mp[0])) and not visited[newx][newy] and mp[newx][newy] < 9:
      basin.append(1)
      count_size(mp, visited, newx, newy, basin)
  return len(basin)


def find_basins(mp):
  visited = [[0 for _ in range(len(mp[0]))] for __ in range(len(mp))]
  basin_sizes = []

  for i in range(len(mp)):
    for j in range(len(mp[0])):
      if mp[i][j] != 9 and not visited[i][j]:
        basin = [1]
        basin_sizes.append(count_size(mp, visited, i, j, basin))

  *_, a, b, c = sorted(basin_sizes)
  return a*b*c


def main():
  data = get_in('input09.txt')
  print(find_low_points(data))
  print(find_basins(data))


if __name__=='__main__':
  main()