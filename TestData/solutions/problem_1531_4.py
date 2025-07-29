class Solution:
    def solution_1531_4(self, s: str) -> int:
        prefix = {"0": 0, "1": 0}
        suffix = {"0": 0, "1": 0}
        for i in s:
            suffix[i] += 1
        res = 0
        
        for i in s:
            complement = "0" if i == "1" else "1"
            suffix[i] -= 1
            res += suffix[complement] * prefix[complement]
            prefix[i] += 1
        return res