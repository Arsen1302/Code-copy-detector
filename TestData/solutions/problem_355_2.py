class Solution:
    def solution_355_2(self, flowerbed: List[int], n: int) -> bool:
        l=[0]+flowerbed+[0]
        for i in range(1,len(l)-1):
            if sum(l[i-1:i+2])==0:
                l[i]=1
                n-=1 
        return n<=0