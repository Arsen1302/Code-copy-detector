class Solution:
    def solution_585_3(self, s: str, k: int) -> str:
        if k==1:
            ans=s
            for i in range(len(s)):
                if ((s+s)[i:i+len(s)])<ans: ans=((s+s)[i:i+len(s)])
            return ans
        else:
            return "".join(sorted(s))