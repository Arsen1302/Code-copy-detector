class Solution:
    def solution_1507_3(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        return sorted(nums, key = lambda x: int("".join([str(mapping[int(digit)]) for digit in str(x)])))