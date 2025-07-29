class Solution:
    def solution_935_3(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        l=len(satisfaction)
        lst=[i+1 for i in range(l)]
        res=0
        i=0
        while(i<l):
            temp=0
            k=i
            for j in range(1,l-i+1):
                temp = temp + satisfaction[k]*j
                k+=1
            res=max(res,temp)
            i+=1
        return res