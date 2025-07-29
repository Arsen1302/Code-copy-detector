class Solution:
    def solution_1587_5(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        ans = []
        potions.sort(reverse=True)

        for i in range(len(spells)):

            l, r = 0, len(potions) - 1
            
            while l <= r:
                p = (l + r) // 2
                if potions[p] * spells[i] >= success:
                    l = p + 1
                else:
                    r = p - 1

            if potions[p] * spells[i] >= success:
                ans.append(p + 1)
            else:
                ans.append(p)
        
        return ans