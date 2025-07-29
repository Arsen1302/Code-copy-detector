class Solution:
    def solution_1302_3(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            if sorted(temp) == temp:
                if len(set(temp)) == len(temp):
                    return True
        return False