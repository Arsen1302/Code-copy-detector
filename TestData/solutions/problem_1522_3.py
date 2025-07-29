class Solution:
    def solution_1522_3(self, nums: List[int]) -> int:
        
        ans = 0
        i = 1
        prev = nums[0]
        flag = False
        
        while i < len(nums) - 1:
            if (nums[i] > prev and nums[i] > nums[i + 1]) or(nums[i] < prev and nums[i] < nums[i + 1]):
                ans += 1
                prev = nums[i]
                print(nums[i])
            elif nums[i] != nums[i+1]:
                prev = nums[i]
            i += 1
        return ans