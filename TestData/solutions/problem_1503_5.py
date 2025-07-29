class Solution:
    def solution_1503_5(self, s: str, t: str) -> int:
        c1,c2=Counter(s),Counter(t)
        c=(c1-c2)+(c2-c1)
        k=0
        for i in c:
            k=k+c[i]
        return (k)