class Solution:
    def solution_1173_2(self, gain: List[int]) -> int:
        ans=[0]
        for i in range(len(gain)):
            ans.append(ans[i]+gain[i])            
        return max(ans)