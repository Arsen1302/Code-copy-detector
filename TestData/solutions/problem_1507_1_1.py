class Solution:
    def solution_1507_1_1(self, mapping: List[int], nums: List[int]) -> List[int]:
        @cache
        def solution_1507_1_2(i: int):
            res, pow10 = 0, 1
            while i:
                res += pow10 * mapping[i % 10]
                i //= 10
                pow10 *= 10
            return res
        return sorted(nums, key=lambda i: mapping[i] if i < 10 else solution_1507_1_2(i))