class Solution:
    def solution_1029_1(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(i for i in res)