class Solution:
    def solution_1333_4(self, neededApples: int) -> int:
        A = neededApples
        x = 0
        curr = 0
        
        while curr < A:
            temp = 0
            x += 1
            # temp = 2*(x-1)*x + x*(x-1) 
            # curr += 4*(temp + 3*x)
            curr += 4*(3*x*x)
        return 4*(2*x)