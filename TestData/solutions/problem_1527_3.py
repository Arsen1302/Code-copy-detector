class Solution:
    def solution_1527_3(self, Q: List[int], k: int) -> List[int]:
        ans=[] ; s='' ; n=ceil(k/2)-1
        for i in Q:
            x=str(10**n+i-1)
            if k%2==0: s=x+x[::-1]
            else: s=x+x[::-1][1:]
            ans.append(s if len(s)==k else -1)
        return ans