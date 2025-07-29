class Solution:
    def solution_1664_3(self, s: str) -> int:
        dict1={}
        res=1
        for i,c in enumerate(s):
            if dict1.get(c,None) is None:
                dict1[c]=c
            else:
                dict1={c:c}
                res+=1
        return res