class Solution(object):
    def solution_86_5(self, n):

        count = 0
        while n:
            count += 1
            n = n &amp; (n - 1)
        
        return count