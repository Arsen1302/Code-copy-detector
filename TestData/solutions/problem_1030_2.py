class Solution:
    def solution_1030_2(self, target: str) -> int:
        ans = flip = 0
        for bulb in target: 
            if flip ^ int(bulb): 
                flip ^= 1
                ans += 1
        return ans