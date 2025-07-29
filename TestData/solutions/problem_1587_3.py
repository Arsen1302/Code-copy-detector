class Solution:
    def solution_1587_3(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions = [math.ceil(success/potion) for potion in reversed(sorted(potions)) ]
        return [bisect_right(potions, spell) for spell in spells]