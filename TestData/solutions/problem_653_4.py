class Solution:
    def solution_653_4(self, s: str, t: str) -> bool:
        fn = lambda x: float(x[:i] + x[i+1:-1] * 17 if (i := x.find('(')) >= 0 else float(x)) 
        return fn(s) == fn(t)