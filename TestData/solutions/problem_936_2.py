class Solution:
    def solution_936_2(self, nums: List[int]) -> List[int]:
        if (len(nums) == 1):
            return nums
        nums.sort()
        count = 0
        num = []
        l = len(nums)
        for i in range(1,l+1):
            count += nums[-i]
            num.append(nums[-i])
            if count > sum(nums[:l-i]):
                return (num)