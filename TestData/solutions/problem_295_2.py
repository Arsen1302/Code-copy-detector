class Solution:
    def solution_295_2(self, num: int) -> bool:
        l=[]
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                l.extend([i,num//i])
        return sum(set(l))-num==num