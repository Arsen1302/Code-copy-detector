class Solution:
    def solution_1687_5(self, pref: List[int]) -> List[int]:
        l=[]
        l.append(pref[0])
        for i in range(1,len(pref)):
            l.append(pref[i-1]^pref[i])
        return l