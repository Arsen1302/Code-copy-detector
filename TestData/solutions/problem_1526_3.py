class Solution:
    def solution_1526_3(self, nums: List[int]) -> int:
        i = index = steps = 0
        while i < len(nums):
            if index%2 != 0:
                index += 1
            else:
                if i == len(nums)-1:
                    index += 1
                    break
                if nums[i] == nums[i+1]:
                    steps += 1
                else:
                    index += 1
            i += 1
        
        return steps if index%2 == 0 else steps+1