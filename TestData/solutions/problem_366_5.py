class Solution(object):
    def solution_366_5(self, c):
        root = int(sqrt(c))
        for i in range(root+1):
            if int(sqrt(c-i*i))**2+i**2 == c:
                return True
        return False