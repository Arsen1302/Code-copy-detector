class Solution:
    def solution_973_4(self, text: str) -> str:
        a=text.split()
        d,t={},''
        for i in a:
            l=len(i)
            if l in d:
                d[l]+=" "+i
            else:
                d[l]=i
        for i in sorted(d):
            t+=" "+d[i]
        t=t.lstrip().capitalize()
        return t