class Solution:
    def solution_1576_3(self, s: str) -> bool:
        for i in range(len(s)):
            c=s.count(str(i))
            if c==int(s[i]):
                continue
            else:
                return False
        return True