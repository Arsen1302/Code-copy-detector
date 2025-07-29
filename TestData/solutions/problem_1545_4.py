class Solution:
    def solution_1545_4(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = [s[x:x+k] for x in range(0, len(s), k)]
            temp = ""
            for i in groups:
                dig = [int(y) for y in i]
                temp += str(sum(dig))
            s = temp
        return s