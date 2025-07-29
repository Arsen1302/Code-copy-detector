class Solution:
    def solution_1549_3(self, nums: List[List[int]]) -> List[int]:
        res = []
        nums = sorted(nums, key=len)
        check = 0
        for i in nums[0]:
            for j in nums:
                if i in j:
                    check += 1
            if check == len(nums):
                res.append(i)
            check = 0
        return sorted(res)