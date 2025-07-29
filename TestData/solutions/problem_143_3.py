class Solution:
    def solution_143_3(self, p: str, s: str) -> bool:
        x=s.split(' ')
        if len(x)!=len(p) : return False
        return len(set(zip(p,x)))==len(set(p))==len(set(x))