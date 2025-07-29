class Solution:
    def solution_1051_4(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        if max(nums) == 0:
            return 0
        while max(nums) != 0:
            for i in range(n):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    count += 1
            for i in range(n):
                nums[i] //= 2
            count += 1
        return count - 1