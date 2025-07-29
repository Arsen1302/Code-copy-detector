class Solution:
    def solution_685_3(self, nums: List[int], k: int) -> int:
        nums.sort(key=abs, reverse=True)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
            if k == 0:
                break
        if k % 2 != 0:
            nums[-1] *= -1
        return sum(nums)
		```