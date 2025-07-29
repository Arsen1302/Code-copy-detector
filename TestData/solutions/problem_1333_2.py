class Solution:
    def solution_1333_2(self, neededApples: int) -> int:
        A = neededApples
        x = 0
        curr = 0
        
        while curr < A:
            temp = 0
            x += 1
            for i in range(1,x):
                temp += ((x+i)*2)
            curr += 4*(temp + 3*x)
        return 4*(2*x)