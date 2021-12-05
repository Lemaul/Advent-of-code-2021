
# '2,1 -> 3,7'      =>     [(2, 1), (3, 7)]
def get_input(file_name):
  with open(file_name) as f:
    vents = f.read().split('\n')
    for i, vent in enumerate(vents):
      v = vent.split(' -> ')
      vents[i] = [tuple(map(int, v[0].split(','))), tuple(map(int, v[1].split(',')))]
    return vents


def part1(vents, diagram_len):
  diagram = [[0 for _ in range(diagram_len)] for __ in range(diagram_len)]
  for vent in vents:
    # [(5, m), (5, n)]
    if vent[0][0] == vent[1][0]:
      start, finish = min(vent[0][1], vent[1][1]), max(vent[0][1], vent[1][1])
      for i in range(start, finish + 1):
        diagram[i][vent[0][0]] += 1
    # [(m, 5), (n, 5)]
    elif vent[0][1] == vent[1][1]:
      start, finish = min(vent[0][0], vent[1][0]), max(vent[0][0], vent[1][0])
      for i in range(start, finish + 1):
        diagram[vent[0][1]][i] += 1
  
  overlapping = 0
  for row in diagram:
    for col in row:
      if col > 1:
        overlapping += 1

  return overlapping, diagram


def part2(vents, lines_diagram):
  for vent in vents:
    if vent[0][0] != vent[1][0] and vent[0][1] != vent[1][1]:
      start_x, finish_x = vent[0][0], vent[1][0]
      start_y, finish_y = vent[0][1], vent[1][1]

      # (0, 0), (8, 8)
      if start_x < finish_x and start_y < finish_y:
        for i in range(start_x, finish_x + 1):
          lines_diagram[start_y + i - start_x][i] += 1

      # (0, 5), (5, 0)
      elif start_x < finish_x and start_y > finish_y:
        for i in range(start_x, finish_x + 1):
          lines_diagram[start_y - i + start_x][i] += 1

      # (5, 5), (2, 8)
      elif start_x > finish_x and start_y < finish_y:
        for i in range(start_y, finish_y + 1):
          lines_diagram[i][start_x - i + start_y] += 1

      # (6, 4), (2, 0)
      elif start_x > finish_x and start_y > finish_y:
        for i in range(start_y, finish_y - 1, -1):
          lines_diagram[i][start_x + i - start_y] += 1

  overlapping = 0
  for row in lines_diagram:
    for col in row:
      if col > 1:
        overlapping += 1

  return overlapping


def main():
  file_location, diagram_len = 'input05.txt', 1000
  vents = get_input(file_location)
  r1, lines_diagram = part1(vents, diagram_len)
  print(r1)
  r2 = part2(vents, lines_diagram)
  print(r2)


if __name__=='__main__':
  main()