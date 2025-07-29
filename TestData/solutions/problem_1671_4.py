class Solution:
    def solution_1671_4(self, n: int) -> int:
        if n % 2 == 0: # check if n is even return as it is because it will be the smallest even no 
            return n
        else:
            return n*2 # else multipy it with 2 to convert it into smallest event multiple