class Solution:
    def solution_638_4(self, c, n) :
        for _ in range(1+(n-1)%14) :
            p=-1
            for i in range(8) : 
                p, c[i] = c[i], int(i<7 and p==c[i+1])
        return c