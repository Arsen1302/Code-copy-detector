class Solution:
    def solution_1682_1(self, a: int, b: int) -> int:
        c=0
        mi=min(a,b)
        for i in range(1,mi+1):
            if a%i==0 and b%i==0:
                c+=1
        return c