class Solution:
	def solution_1029_2(self, s: str, indices: List[int]) -> str:
		result = [""] * len(s)

		for i, letter in enumerate(s):
			result[indices[i]] = letter

		return "".join(result)