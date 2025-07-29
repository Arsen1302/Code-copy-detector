class Solution:
    def solution_1333_5(self, neededApples: int) -> int:
        A = neededApples
        x = 0
        curr = 0
        
        while curr < A:
            x += 1
            curr = 2*(x)*(x+1)*(2*x+1)
        return 4*(2*x)