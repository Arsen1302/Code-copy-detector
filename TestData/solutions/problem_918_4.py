class Solution:
	def solution_918_4(self, mat: List[List[int]]) -> List[int]:
		return list({min(row) for row in mat} &amp; {max(col) for col in zip(*mat)})