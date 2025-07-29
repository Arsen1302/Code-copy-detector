class Solution:
    def solution_791_1_1(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(max(nums), 0)
    
    def solution_791_1_2(self, arr: List[int], k: int) -> int:
        sums = sum(arr)
        mod = 10**9 + 7
        if k == 1:
            return self.solution_791_1_1(arr) % (mod)
        if sums > 0:
            return (self.solution_791_1_1(arr+arr) + (k-2)*sums) % (mod)
        else:
            return self.solution_791_1_1(arr+arr) % (mod)