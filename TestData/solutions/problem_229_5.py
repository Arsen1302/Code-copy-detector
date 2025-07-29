class Solution:
	def solution_229_5(self, nums: List[int]) -> int:

		maxvalue = 0
		mask = 0;

		newset = set()

		for i in range(30, -1, -1):

			mask = mask | (1 << i)
			newMaxvalue = maxvalue | (1 << i)

			for i in range(len(nums)):

				newset.add(nums[i] &amp; mask)

			for prefix in newset:

				if (newMaxvalue ^ prefix) in newset:
					maxvalue = newMaxvalue
					break

			newset.clear()

		return maxvalue