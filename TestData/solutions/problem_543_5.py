class Solution(object):
    def solution_543_5(self, S):
        """
        :type S: str
        :rtype: int
        """
        res, balance = 0, 0
        for index, ch in enumerate(S):
            balance = balance+1 if ch == '(' else balance-1
            if index and S[index-1] + ch == '()':
                res += 2 ** balance
        return res