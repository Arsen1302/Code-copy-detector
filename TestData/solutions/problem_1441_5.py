class Solution:
    def solution_1441_5(self, nums: List[int]) -> int:
        summ = 0
        for i in range(len(nums)):
            maxx = nums[i]
            minn = nums[i]
            for j in range(i+1, len(nums)):
                maxx = max(maxx, nums[j])
                minn = min(minn, nums[j])
                summ += (maxx-minn)
        return summ