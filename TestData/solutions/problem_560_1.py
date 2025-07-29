class Solution:
    def solution_560_1(self, arr: List[int]) -> int:
        arrset=set(arr)
        res=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                a,b,l=arr[i],arr[j],2
                while(a+b in arrset):
                    a,b,l=b,a+b,l+1
                res=max(res,l)
        return res if res>=3 else 0