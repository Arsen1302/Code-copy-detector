class Solution:
    def solution_1097_3(self, s: str) -> int:
        occ=dict()
        mx=-1
        for i in range(0,len(s)):
            if s[i] in occ.keys():
                if i-occ[s[i]]-1>mx:
                    mx=i-occ[s[i]]-1
            else:
                occ.update({s[i]:i})
        return mx