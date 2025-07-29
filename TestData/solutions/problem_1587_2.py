class Solution:
    def solution_1587_2(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        return [N - bisect_left(potions, success / x) for x in spells]