class Solution:
    def solution_1687_3(self, pref: List[int]) -> List[int]:
        ans = [pref[0]] * len(pref)
        
        for i in range(1,len(ans)):
            ans[i] = pref[i] ^ pref[i-1]
        return (ans)