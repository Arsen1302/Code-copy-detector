class Solution:
    def solution_732_4(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        if m == n:
            if str1 == str2:
                return str1
            else:
                return ""
        elif m > n:
            if str1[ : n] != str2:
                return ""
            else:
                return self.solution_732_4(str1[n : ], str2)
        else:
            if str2[ : m] != str1:
                return ""
            else:
                return self.solution_732_4(str2[m : ], str1)