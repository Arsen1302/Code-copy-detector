class Solution:
    def solution_1180_1(self, n: int) -> int:
        x = int((6*n)**(1/3))
        if x*(x+1)*(x+2) > 6*n: x -= 1
        
        ans = x*(x+1)//2
        n -= x*(x+1)*(x+2)//6
        k = 1
        while n > 0: 
            ans += 1
            n -= k
            k += 1
        return ans