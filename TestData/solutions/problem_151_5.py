class Solution:
		def solution_151_5(self, nums: List[int]) -> int:
			dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
			# fill the (0,0), (1,1) etc
			for i in range(len(nums)):
				dp[i][i] = nums[i]*(nums[i-1] if i-1>=0 else 1)*(nums[i+1] if i+1<len(nums) else 1)

			for offset in range(1,len(nums)):
				x = 0
				while x+offset<len(nums):
					y = x + offset
					curr = 0
					for j in range(x,y+1):
						left = 0 if j-1<x else dp[x][j-1]
						mid =  (nums[x-1] if x-1>=0 else 1)*nums[j]*(nums[y+1] if y+1<len(nums) else 1)
						right = 0 if j+1>y else dp[j+1][y]
						dp[x][y] = max(dp[x][y],left + mid + right)
					x+=1
			return dp[0][-1]