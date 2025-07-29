class Solution:
	def solution_1043_4(self, nums: List[int], target: int) -> int:
		dp = defaultdict(int)
		dp[0] = 1
		curSum = 0
		result = 0

		for i in range(len(nums)):
			curSum += nums[i]

			if curSum - target in dp:
				result += dp[curSum-target]

				dp = defaultdict(int)
				dp[0] = 1
				curSum = 0

			dp[curSum] = 1

		return result