class Solution:
    def solution_1242_5(self, nums) -> int:
        count=0
        value=0
        for i in range(len(nums)-1):
            if nums[i+1] <= nums[i]:
                value = (nums[i]+1) -nums[i+1]
                nums[i+1] +=value
                count+=value

        return count