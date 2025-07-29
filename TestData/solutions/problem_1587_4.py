class Solution:
    def solution_1587_4(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        len_p = len(potions)
        return [len_p - bisect_left(potions, ceil(success / s)) for s in spells]