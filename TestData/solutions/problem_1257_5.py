class Solution:
    def solution_1257_5(self, nums: List[int], target: int, start: int) -> int:
            x = len(nums)+1;
            for i in range(0 , len(nums)):
                if(nums[i] == target):
                    x = min(x ,abs(start-i));
            return x;