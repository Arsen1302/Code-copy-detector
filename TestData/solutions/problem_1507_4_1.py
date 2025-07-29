class Solution:
    def solution_1507_4_1(self, mapping: List[int], nums: List[int]) -> List[int]:
        m = { str(i): str(v) for i, v in enumerate(mapping) }

        def solution_1507_4_2(n):
            return int(''.join(m[i] for i in str(n)))
                
        return sorted(nums, key=solution_1507_4_2)