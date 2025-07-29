class Solution:
    def solution_1173_5(self, gain: List[int]) -> int:
        high = max(0,gain[0])
        tmp = gain[0]
        for i in range(1,len(gain)):
            tmp += gain[i]
            high = max(tmp,high)
        return high