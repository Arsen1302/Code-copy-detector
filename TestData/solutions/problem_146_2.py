# Pure Dynamic Proramming Solution
# Time : O(n*(n+1)/2) - O(n^2)
# Space: O(n)
class Solution:
	def solution_146_2(self, nums: List[int]) -> int:
		n = len(nums)
		dp = [0]*n
		for i in range(n):
			maX = 0
			for j in range(i+1):
				if nums[j] < nums[i]:
					if dp[j] > maX:
						maX = dp[j]
			dp[i] = maX+1
		return max(dp)

# Dynamic Programming with Binary Search
# Time: O(nlogn), logn for searching the position for the element's and there are n steps.
# Space: O(n)
from bisect import bisect_left
class Solution:
	def solution_146_2(self, nums):
		dp = []
		for elem in nums:
			idx = bisect_left(dp, elem)
			if idx == len(dp):
				dp.append(elem)
			else:
				dp[idx] = elem
		return len(dp)

# Dynamic Programming with Binary Search
# Time: O(nlogn), logn for searching the position for the element's and there are n steps.
# Space: O(1)
from bisect import bisect_left
class Solution:
	def solution_146_2(self, nums: List[int]) -> int:
		n = len(nums)
		for i in range(n):
			# Here we pass three arg's, which means find the position of nums[i] in the nums array within index i.
			idx = bisect_left(nums, nums[i], hi=i)
			if idx != i:
				nums[idx], nums[i] = nums[i], float(inf)
		return nums.index(float(inf)) if float(inf) in nums else n