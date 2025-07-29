class Solution:
    def solution_1584_4(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        # print(nums)
        initial = nums[0]
        count = 0
        for i in range(1, len(nums)):
            if initial - nums[i] > k:
                initial = nums[i]
                count += 1
        count += 1
        return count