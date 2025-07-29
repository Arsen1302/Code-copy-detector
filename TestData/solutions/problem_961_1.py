class Solution:
    def solution_961_1(self, nums: List[int], k: int) -> bool:
        indices = [i for i, x in enumerate(nums) if x == 1]
        if not indices:
            return True
        for i in range(1, len(indices)):
            if indices[i] - indices[i-1] < k + 1:
                return False
        return True