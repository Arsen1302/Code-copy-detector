class Solution:
    def solution_410_1(self, n: int) -> bool:
        s = bin(n).replace('0b','')
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return False
        return True