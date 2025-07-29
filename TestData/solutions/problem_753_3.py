class Solution:
	def solution_753_3(self, bookings: List[List[int]], n: int) -> List[int]:

		result = [0]*n
		for start, end, value in bookings:
			result[start-1] += value
			if end < n:
				result[end] -= value

		for index, value in enumerate(result):
			if index != 0:
				result[index] += result[index-1]

		return result