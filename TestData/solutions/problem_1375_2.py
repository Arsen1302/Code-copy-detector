class Solution:
    def solution_1375_2(self, a: List[int]) -> int:
        temp,temp2=a[0],a[-1]
        left=([a[0]]+[0]*(len(a)-1))
        right=[0]*(len(a)-1) + [a[-1]]
        for i in range(1,len(a)):
            left[i]=max(a[i-1],temp)
            temp=left[i]
        for i in range(len(a)-2,-1,-1):
            right[i]=min(a[i+1],temp2)
            temp2=right[i]
        res=0
        for i in range(1,len(a)-1):
            if(a[i]>left[i] and a[i]<right[i]):
                res+=2
            elif(a[i]>a[i-1] and a[i]<a[i+1]):
                res+=1
        return res