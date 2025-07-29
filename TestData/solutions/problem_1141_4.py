class Solution:
    def solution_1141_4(self, n: int) -> int:
        i=n
        c=0
        while i!=1:
            if(i%2==0):
                c+=i//2
                i=i//2
            else:
                c+=(i-1)//2
                i=(i-1)//2 +1
        return c