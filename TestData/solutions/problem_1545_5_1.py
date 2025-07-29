class Solution:
    def solution_1545_5_1(self, s: str, k: int) -> str:
        def solution_1545_5_2(s):
            return str(sum([int(i) for i in s]))

        if len(s) <= k:
            return s
        tmp = []
        for i in range(0, len(s), k):
            tmp.append(solution_1545_5_2(s[i:i + k]))
        s = ''.join(tmp)
        return self.solution_1545_5_1(s, k)