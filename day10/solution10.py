
def get_brackets(file):
  with open(file) as f:
    return f.read().split()


def solve(lines):
  scores = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
  }
  brackets = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
  }

  faults = 0
  autocompletion_scores = []
  for line in lines:
    s = []
    for c in line:
      if c in brackets.keys():
        s.append(c)
      elif c == brackets[s[-1]]:
        s.pop(-1)
      else:
        faults += scores[c]
        s = []
        break

    if len(s) > 0:
      curr = 0
      autocomplete = {
        '(' : 1,
        '[' : 2,
        '{' : 3,
        '<' : 4
      }
      for c in s[::-1]:
        curr *= 5
        curr += autocomplete[c]
      autocompletion_scores.append(curr)

  return faults, sorted(autocompletion_scores)[len(autocompletion_scores) // 2]



def main():
  lines = get_brackets('input10.txt')
  r1, r2 = solve(lines)
  print(r1, r2)


if __name__=='__main__':
  main()