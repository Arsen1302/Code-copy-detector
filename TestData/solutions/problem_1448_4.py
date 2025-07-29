class Solution:
    def solution_1448_4(self, sentences: List[str]) -> int:
        ans=0
        for i in sentences:
            ans=max(ans,i.count(' '))
        return ans+1