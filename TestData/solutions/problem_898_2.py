class Solution:
	def solution_898_2(self, array: List[int]) -> List[int]:

		array = sorted(array)

		d = {}

		for i in array:

			total_one = bin(i)[2:].count('1')

			if total_one not in d:
				d[total_one] = [i]
			else:
				d[total_one].append(i)

		d = dict(sorted(d.items() , key = lambda x:x[0]))

		result = []

		for key in d:
			result = result + d[key]

		return result