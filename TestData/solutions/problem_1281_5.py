class Solution:
    def solution_1281_5(self, n: str, x: int) -> str:
        if n[0] == '-':
            for i in range(1,len(n)):
                if int(n[i]) > x:
                    return n[:i] + str(x) + n[i:]
            else: return n + str(x)
        else:
            if int(n[0]) < x:
                return str(x) + n 
            for i in range(len(n)):
                if int(n[i]) < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)