class Solution:
    def solution_664_2(self, a: int, b: int) -> str:
        ans = []
        while a and b: 
            if ans[-2:] == ["b"]*2 or 2*b < a: 
                ans.append("a")
                a -= 1
            else: 
                ans.append("b")
                b -= 1
        ans.extend(a*["a"] + b*["b"])
        return "".join(ans)