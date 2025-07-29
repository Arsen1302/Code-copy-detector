class Solution:
    def solution_1507_5(self, mapping: List[int], nums: List[int]) -> List[int]:
        m = { str(i): str(v) for i, v in enumerate(mapping) }
        return sorted(nums, key=lambda x: int(''.join(m[i] for i in str(x))))