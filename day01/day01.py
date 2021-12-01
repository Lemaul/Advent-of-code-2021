
def get_numbers(file_path):
  with open(file_path)as f:
    return list(map(int, f.read().split('\n')))


def count_increases(measurements):
  prev = measurements[0]
  result = 0
  for depth in measurements:
    result += depth > prev
    prev = depth

  return result


def count_sum_increases(measurements):
  prev = sum(measurements[:3:])
  result = 0
  for i in range(3, len(measurements)):
    result += prev < prev - measurements[i - 3] + measurements[i]
    prev = prev - measurements[i - 3] + measurements[i]
  
  return result 



def main():
  file = 'day01.txt'
  measurements = get_numbers(file)
  # print(count_increases(measurements))
  print(count_sum_increases(measurements))


if __name__=='__main__':
  main()