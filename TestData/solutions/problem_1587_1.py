class Solution:
    def solution_1587_1(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans, n = [], len(potions)
        for spell in spells:
            val = success // spell
            if success % spell == 0:
                idx = bisect.bisect_left(potions, val)
            else:    
                idx = bisect.bisect_right(potions, val)
            ans.append(n - idx)
        return ans