class Solution:
    def solution_1007_3_1(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        ct = 0
        
        n = len(nums)
        nums.sort()
        
        def solution_1007_3_2(x: List[int], t: int, l: int, n: int = n) -> int:
			# Returns the rightmost valid index for number <= target
            r = n-1
            while(l < r):
                m = l + (r - l) // 2 + 1
                if x[m] <= t:
                    l = m
                else:
                    r = m - 1
            return r
        
		# loop on min value
        for i in range(n):
            if 2 * nums[i] > target:
				# no need to process further (sorted array)
                break 
				
            # find max j for valid subarray
            j = solution_1007_3_2(nums, target - nums[i], i)
            if nums[i] + nums[j] <= target:
				# add 1 * 2^((j - i + 1) - 1) for no. of subsets 
				# from subarray with one element fixed
                ct += pow(2 , j - i, mod)  # for efficient handling of large no.s
        return ct % mod