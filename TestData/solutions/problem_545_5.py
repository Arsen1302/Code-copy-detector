class Solution:
    def solution_545_5(self, p: int, q: int) -> int:
        '''
          Using simple geometry and just by observing we can decide where
          will the ray hit. for example:
          p = 2, q = 1; the ray first meets 2nd receptor after it gets reflected
          for 1 time
          p = 3, q = 1; the ray first meets 1st receptor after it gets reflected
          for 2 times.
          From the given examples one can easly observe that
          1:if p is even and q is odd, it'll surely hit 2nd receptor for the first
          time
          2:if both p and q is odd, it'll surely hit 1st receptor for the first time
          
        '''
        # base case if both p and q are equal, it will always hit receptor 1,
        # irrespective of their nature
        if p == q: 
            return 1
        
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2
            
        if p % 2 == 1 and q % 2 == 0:
            return 0
        elif p % 2 == 1 and q % 2 == 1:
            return 1
        elif p % 2 == 0 and q % 2 == 1:
            return 2