class Solution:
    def solution_1622_1(self, nums: List[int]) -> int:
        
        n = len(nums)

        ans = 0
        i, j = 0, 0
        while i <= n - 1:
            j = 0
            if nums[i] == 0:
                while i + j <= n - 1 and nums[i + j] == 0:
                    j += 1
                ans += (j + 1) * j // 2

            i = i + j + 1
        
        return ans