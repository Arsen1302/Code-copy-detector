class Solution:
    def solution_1687_2(self, pref: List[int]) -> List[int]:
        xor = 0
        ans = []
        for i in range(len(pref)):
            ans.append(pref[i]^xor)
            xor ^= ans[i]
        return ans