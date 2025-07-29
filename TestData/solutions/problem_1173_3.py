class Solution:
    def solution_1173_3(self, gain: List[int]) -> int:
        ans = max(0, gain[0])
        for i in range(1, len(gain)):
            gain[i] = gain[i-1] + gain[i]
            if gain[i] > ans:
                ans = gain[i]
        return ans