
def get_input(file_name):
  with open(file_name) as f:
    return list(map(int, f.read().split(',')))


def min_fuel_1(positions):
  srtd = sorted(positions)
  l = len(positions)
  median = srtd[l//2] if not l % 2 else (srtd[l//2] + srtd[l//2+1]) / 2
  
  return sum(abs(pos - median) for pos in positions)


def min_fuel_2(positions):
  avg = round(sum(positions) / len(positions))
  dst = lambda i, pos: abs(pos - i) * (abs(pos - i)+1) // 2
  # avg-10, avg+10 range is close enough
  return min( sum( dst(i, pos) for pos in positions ) for i in range(avg-10, avg+10) )


def main():
  data = get_input('input07.txt')
  print(min_fuel_1(data))
  print(min_fuel_2(data))


if __name__=='__main__':
  main()