class Solution:
    def solution_1077_5_1(self, s: str) -> int:
        def solution_1077_5_2(s, soFar=set()):
            if len(s) == 1 and s in soFar:
                return 0
            maxSplit = len(soFar)+1
            for partition in range(1, len(s)):
                a = s[:partition]
                b = s[partition:]
                if a not in soFar:
                    maxSplit = max(maxSplit, solution_1077_5_2(b, soFar|{a}))
            return maxSplit
        return solution_1077_5_2(s)