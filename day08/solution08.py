
def get_input(file):
  with open(file) as f:
    data = f.read().split('\n')
    for i, d in enumerate(data):
      data[i] = d.split(' | ')
      data[i][0] = data[i][0].split()
      data[i][1] = data[i][1].split()
    return data


def part1(data):
  acc = [2, 3, 4, 7]
  r1 = 0
  for d in data:
    for n in d[1]:
      if len(n) in acc:
        r1 += 1
  return r1


def main():
  data = get_input('input08.txt')
  print(data[0])
  print(part1(data))


if __name__=='__main__':
  main()