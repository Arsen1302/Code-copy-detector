class Solution:
    def solution_889_5(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        res=0
        s=sum(arr[:k])
        if s/k>=threshold:
            res+=1
        
        for i in range(1,n-k+1):
            s-=arr[i-1]
            s+=arr[i+k-1]
            if s/k>=threshold:
                res+=1
        
        return res