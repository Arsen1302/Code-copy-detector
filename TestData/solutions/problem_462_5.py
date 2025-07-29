class Solution:
	def solution_462_5(self, arr: list[int]) -> int:
		max_chunk = 0

		min_left_i = [float('inf')]*(len(arr)+1)
		curr_min = math.inf

		# find the 
		for i in range(len(arr)-1, -1, -1):
			if arr[i] < curr_min:
				curr_min = arr[i]
			min_left_i[i] = curr_min


		max_till_i = arr[0]
		for i in range(len(arr)):
			if arr[i] > max_till_i:
				max_till_i = arr[i]

			# check to verify if there is no element to the right which is lower than the current.
			if max_till_i <= min_left_i[i+1]:
				max_chunk += 1

		return max_chunk