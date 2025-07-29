class Solution:
    def solution_965_4(self, arr: List[int]) -> int:
        n=len(arr)
        prefix=[0 for i in range(n)]
        ans=0
        for i in range(n):
            prefix[i]=prefix[i-1]^arr[i] if i>=1 else arr[i]
            cnt=0
            for j in range(i-1):
                if prefix[i]==prefix[j]:
                    cnt+=i-j-1
            if prefix[i]==0:
                cnt+=i
            ans+=cnt
        return ans