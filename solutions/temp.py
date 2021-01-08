def solve(st):
  return solve_helper(st, 0, len(st)-1)

def solve_helper(st, start_index, end_index):
    # we don't need to cut the string if it is a palindrome
    if start_index >= end_index or is_palindrome(st, start_index, end_index):
        return 0

    # at max, we need to cut the string into its 'length-1' pieces
    min_cuts=end_index-start_index
    for i in range(start_index,end_index+1):
        if is_palindrome(st,start_index,i):
            # we can cut here as we have a palindrome from 'startIndex' to 'i'
            min_cuts=min(min_cuts,1+solve_helper(st,i+1,end_index))

    return min_cuts


def is_palindrome(st, x, y):
  while (x < y):
    if st[x] != st[y]:
      return False
    x += 1
    y -= 1
  return True

print(solve("racecarannakayak"))
#   print(solve("cdpdd"))
#   print(solve("pqr"))
#   print(solve("pp"))
#   print(solve("madam"))