class Solution:
	def solution_1583_4(self, nums: List[int]) -> int:

		if len(nums) ==1:
			return nums[0]

		while len(nums)>1:

			length =len(nums)//2

			temp_array = []

			for i in range(length):

				if i%2==0:
					temp_array.append(min(nums[2 * i], nums[2 * i + 1]))
				else:
					temp_array.append(max(nums[2 * i], nums[2 * i + 1]))

			nums = temp_array

		return nums[0]