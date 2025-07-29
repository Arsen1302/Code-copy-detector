class Solution:
       def solution_222_1(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            j = i+1
            while(j<len(nums)-1):
                if nums[j]-nums[j-1] == nums[j+1]-nums[j]:
                    count += 1
                    j += 1
                else:
                    break
        return count