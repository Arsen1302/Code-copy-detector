class Solution:
    def solution_501_1_1(self, nums: List[int], k: int) -> float:
        
        @lru_cache(maxsize=None)
        def solution_501_1_2(index: int, partitions_left: int) -> int:
            if partitions_left == 1:
                return sum(nums[index:]) / (len(nums) - index)

            max_sum: float = 0.0
            for i in range(index, len(nums) - (partitions_left - 1)):
                cur_sum: float = sum(nums[index:i + 1])/(i + 1 - index)
                cur_sum += solution_501_1_2(i + 1, partitions_left - 1)
                max_sum = max(cur_sum, max_sum)
            return max_sum
    
        return solution_501_1_2(0, k)