class Solution:
    def solution_1594_4(self, s: str) -> str:
        l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for i in l[::-1]:
            if i.lower() in s and i in s:
                return i
        return ""