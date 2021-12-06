
def get_input(file_name):
  with open(file_name) as f:
    return list(map(int, f.read().split(',')))


def get_day_n(day1, n):
  # initial state
  fish = [0 for _ in range(9)]
  for f in day1:
    fish[f] += 1

  for _ in range(n):
    # this is how many fish will be spawned (timer of 8) and reset (timer of 6)
    transforming = fish[0]
    fish[0] = 0
    for f in range(1, 9):
      fish[f - 1] = fish[f]
      fish[f] = 0
    fish[6] += transforming
    fish[8] += transforming

  return sum(fish)     


def main():
  day1 = get_input('input06.txt')
  r1, r2 = get_day_n(day1, 80), get_day_n(day1, 256)
  print(r1, r2)
  

if __name__=='__main__':
  main()
