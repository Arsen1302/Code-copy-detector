class Solution:
    def solution_1700_3_1(self, nums, cost, target):
        res = 0
        for n, c in zip(nums, cost):
            res += abs(n - target) * c
        return res
    
    def solution_1700_3_2(self, nums: List[int], cost: List[int]) -> int:
        s, e = min(nums), max(nums)
        
        while s < e:
            mid = (s + e) // 2
            leftSum, rightSum = self.solution_1700_3_1(nums, cost, mid), self.solution_1700_3_1(nums, cost, mid + 1)
            if leftSum < rightSum:
                e = mid
            else:
                s = mid + 1
        
        return self.solution_1700_3_1(nums, cost, s)