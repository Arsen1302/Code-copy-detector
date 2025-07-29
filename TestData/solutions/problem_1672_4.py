class Solution:
    def solution_1672_4(self, s: str) -> int:
        x=set()
        p=[s[0]]
        for i in s[1:]:
            if ord(p[-1])+1==ord(i):
                p.append(i)
            else:
                x.add("".join(p))
                p=[i]
        x.add("".join(p))
        ans=sorted(x,key=len)[-1]
        return len(ans)