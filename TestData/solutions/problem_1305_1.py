class Solution:
    def solution_1305_1(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]*nums[-2])-(nums[0]*nums[1])