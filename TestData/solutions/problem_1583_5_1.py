class Solution:
    def solution_1583_5_1(self, nums: List[int]) -> int:
        def solution_1583_5_2(nums):
            newNums = []
            n = len(nums)
            a = 0
            while n > 2 * a:
                while a < n / 2:
                    if a % 2 == 0:
                        newNums.append(min(nums[2 * a], nums[2 * a + 1]))
                        a += 1
                    else:
                        newNums.append(max(nums[2 * a], nums[2 * a + 1]))
                        a += 1
            return newNums

        n = len(nums)
        while n > 1:
            nums = solution_1583_5_2(nums)
            n = len(nums)
            
        return nums[0]