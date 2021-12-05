
def get_input(file_name):
  with open(file_name) as f:
      boards = f.read().split('\n\n')

      numbers = boards[0].split(',')
      boards.remove(boards[-len(boards)])
      return numbers, boards


def sum_board(board):
  b_sum = 0
  for row in board:
    for n in row:
      if n != 'X':
        b_sum += int(n)

  return b_sum


def bingo(numbers, boards):
  for i, board in enumerate(boards):
    boards[i] = board.split('\n')
    for j, row in enumerate(boards[i]):
      boards[i][j] = row.split()
  
  win_first = False
  win_sum_first = 0
  win_sum_last = 0
  wins = [0 for _ in boards]
  for num in numbers:
    for i, board in enumerate(boards):
      for j, row in enumerate(board):
        boards[i][j] = ['X' if num == n else n for n in row]
      for j, row in enumerate(board):
        if row.count('X') == len(row) or [r[j] for r in board].count('X') == len(row):
          # first part solution
          if not win_first:
            win_sum_first = int(num) * sum_board(board)
            win_first = True
          wins[i] = 1
          if (sum(wins) == len(boards)):
            win_sum_last = int(num) * sum_board(board)
            return win_sum_first, win_sum_last



def main():
  numbers, boards = get_input('input04.txt')
  r1, r2 = bingo(numbers, boards)
  print(r1, r2)

if __name__=='__main__':
  main()
  