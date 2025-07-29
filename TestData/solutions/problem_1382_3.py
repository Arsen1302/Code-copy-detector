class Solution:
    def solution_1382_3(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res = nums[i] + nums[j]
                    if target == res:
                        count += 1
        return count