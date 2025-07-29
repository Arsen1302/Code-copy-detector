class Solution:
    def solution_1281_3(self, n: str, x: int) -> str:
        for i,val in enumerate(n):
            if n[0] != "-":
                if int(val) < x:
                    return n[:i] + str(x) + n[i:]
            else:
                if val !='-' and int(val) > x:
                    return n[:i] + str(x) + n[i:]
        return n + str(x)