class Solution:
    def solution_714_3(self, nums1: List[int], nums2: List[int]) -> int:
        rows, cols = len(nums1) + 1, len(nums2) + 1
        dp = [[0 for c in range(cols)]for r in range(rows)]
        
        for r in range(1,rows):
            for c in range(1,cols):
                if nums1[r-1] == nums2[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]
#TC: O(m*n) || SC: O(m*n) || m = len(nums1), n = len(nums2)