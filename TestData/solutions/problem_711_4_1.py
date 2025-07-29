class Solution:
    # O(n^2) time,
    # O(1) space,
    # Approach: prefix sum
    def solution_711_4_1(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        max_sum = 0
        
        for i in range(1, n):
            nums[i] += nums[i-1]
            
        def solution_711_4_2(l: int, r: int) -> int:
            if l == 0:
                return nums[r]
            
            return nums[r] - nums[l-1]
        
        for i in range(0, n-firstLen+1):
            first_tot = solution_711_4_2(i, i+firstLen-1)
            for j in range(0, i-secondLen+1):
                second_tot = solution_711_4_2(j, j+secondLen-1)
                max_sum = max(max_sum, second_tot + first_tot)
                
            for j in range(i+firstLen, n-secondLen+1):
                second_tot = solution_711_4_2(j, j+secondLen-1)
                max_sum = max(max_sum, second_tot + first_tot)
                
        return max_sum