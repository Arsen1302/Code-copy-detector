class Solution:
	def solution_1674_1(self, words: List[str]) -> List[int]:

		d = defaultdict(int)

		for word in words:
			for index in range(1, len(word) + 1):
				d[word[:index]] += 1 

		result = []

		for word in words:
			current_sum = 0

			for index in range(1, len(word) + 1):
				current_sum = current_sum + d[word[:index]]

			result.append(current_sum)

		return result