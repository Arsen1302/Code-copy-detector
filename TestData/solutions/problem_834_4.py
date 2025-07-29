class Solution:
    def solution_834_4(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2:
            return []
        jumbo = tomatoSlices // 2 - cheeseSlices
        if jumbo < 0 or cheeseSlices < jumbo:
            return []
        return [jumbo, cheeseSlices - jumbo]