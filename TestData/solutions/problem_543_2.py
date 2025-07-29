class Solution:
    def solution_543_2(self, S: str) -> int:
        res, balance = 0, 0
        for index, par in enumerate(S):
            balance += 1 if par == "(" else -1
            if index and S[index - 1] + par == "()":
                res += 2 ** balance
        return res