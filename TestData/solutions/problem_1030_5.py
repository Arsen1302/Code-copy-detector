class Solution:
    def solution_1030_5(self, target: str) -> int:
        res = 0
        prev = '0'

        for idx in range(len(target)):
            if target[idx] != prev:
                prev = target[idx]
                res += 1
        
        return res