class Solution:
    def solution_1039_1(self, s: str) -> int:
        """
        (
        """
        res = need = 0

        for i in range(len(s)):
            if s[i] == '(':
                need += 2
                if need % 2 == 1:
                    res += 1
                    need -= 1
            if s[i] == ')':
                need -= 1
                if need == -1:
                    res += 1
                    need = 1
        return res + need