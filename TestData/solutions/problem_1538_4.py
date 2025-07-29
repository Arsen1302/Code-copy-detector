class Solution:
    def solution_1538_4(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        cum_sum = 0
        i = 0
        n = len(nums)
		# iterate from smallest to largest nums and stop when the void until that point can hold k units of water
        while True:
            cum_sum += nums[i]
            if i + 1 < n:
				# v = max water supported | nums[i + 1] * (i + 1)  = volume  |  cum_sum is volume already taken
                v = nums[i + 1] * (i + 1) - cum_sum
                if k <= v: # water can fill in the available space
                    break
            else: # case where water fills up over the max num
                v = nums[i] * (i + 1) - cum_sum
                break
            i += 1

        mod = int(10**9) + 7
        op = 1
		
		# since here we add discrete units of water, we must have a base water level and residual can be added over few bins
        min_val = (cum_sum + k) // (i + 1)
        residual = (cum_sum + k) % (i + 1)
        # compute product for water sections
		for j in range(i + 1):
            op = (op * (min_val + (j < residual))) % mod
        # compute product for remaining sections
		if k <= v:
            for j in range(i + 1, n):
                op = (op * nums[j]) % mod
        return op