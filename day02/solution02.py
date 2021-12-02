from collections import defaultdict


def get_input(file_path):
  with open(file_path)as f:
    return [(step.split(' ')[0], int(step.split(' ')[1])) for step in list(f.read().split('\n'))]


def get_position_product(data):
  sums = defaultdict(int)
  for direction, step in data:
    sums[direction] += step
  return sums['forward'] * (sums['down'] - sums['up'])


def get_position_product_with_aim(data):
  forward = aim = depth = 0
  for direction, step in data:
    if direction == 'forward':
      forward += step
      depth += step * aim
    elif direction == 'down':
      aim += step
    else:
      aim -= step
  return forward * depth


def main():
  file = 'input02.txt'
  data = get_input(file)
  print(get_position_product(data))
  print(get_position_product_with_aim(data))


if __name__=='__main__':
  main()