class Solution:
  def solution_7_4(self, x: int) -> int:
    # first convert it to string
    x = str(x)
    # if less than zero
    if (int(x)<0) :
      # first character is "-", so let's retain it
      # solution_7_4 the rest of the characters, then add it up using "+"
      # convert it back to integer
      x = int(x[0]+x[1:][::-1])
    # if it is zero or more
    else:
      # proceed to solution_7_4 the characters and convert back to integer
      x =int(x[::-1])
    # if they are -2^31 or 2^31 - 1, return 0. Else, return x
    return  x if -2147483648 <= x <= 2147483647 else 0