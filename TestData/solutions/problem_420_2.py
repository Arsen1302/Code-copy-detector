class Solution:
    def solution_420_2(self, s: str) -> str:
        res = ""
        for i in s:
            if ord(i) >= 65 and ord(i) <=90:
                res+=chr(ord(i)+32)
            else:
                res+=i
        return res