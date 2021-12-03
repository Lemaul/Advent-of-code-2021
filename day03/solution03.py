
def get_input(file_path):
  with open(file_path)as f:
    return f.read().split('\n')

def get_power(data):
  gamma = ''
  epsilon = ''
  ratios = []
  for current_bit in range(len(data[0])):
    ratios.append( sum((int(binary[current_bit]) for binary in data)) / len(data) )
  
  for ratio in ratios:
    if ratio > 0.5:
      gamma += '1'
      epsilon += '0'
    else:
      gamma += '0'
      epsilon += '1'
  return int(gamma, 2) * int(epsilon, 2)


def get_rating(data, data2):
  for current_bit in range(len(data[0])):
    current_bit_pos_ratio = sum((int(binary[current_bit]) for binary in data)) / len(data)
    current_bit_pos_ratio_2 = sum((int(binary[current_bit]) for binary in data2)) / len(data2)
    current = 1 if current_bit_pos_ratio >= 0.5 else 0
    current2 = 0 if current_bit_pos_ratio_2 >= 0.5 else 1

    if len(data) > 1:
      for binary in data[:]:
        if current != int(binary[current_bit]):
          data.remove(binary)
    if len(data2) > 1:
      for binary in data2[:]:
        if current2 != int(binary[current_bit]):
          data2.remove(binary)
  return int(data[0], 2) * int(data2[0], 2)


def main():
  data = get_input('input03.txt')
  data2 = get_input('input03.txt')
  print(get_power(data))
  print(get_rating(data, data2))


if __name__=='__main__':
  main()