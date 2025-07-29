class Solution:
	def solution_753_5(self, bookings: List[List[int]], n: int) -> List[int]:
		result = [0] * n

		for start, end, val in bookings:
			result[start-1] += val
			if end < n:
				result[end] -= val

		for idx, val in enumerate(result):
			if idx != 0:
				result[idx] += result[idx-1]

		return result