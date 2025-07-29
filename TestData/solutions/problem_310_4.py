class Solution:
	def solution_310_4(self, nums: List[int]) -> int:
		dp = defaultdict(int)
		dp[0] = -1
		curSum = 0
		result = 0

		for i in range(len(nums)):
			if nums[i] == 1:
				curSum += 1

			else:
				curSum -= 1

			if curSum not in dp: # store leftmost idx for longest subarray
				dp[curSum] = i

			else:
				if i - dp[curSum] > result:
					result = i - dp[curSum]

		return result