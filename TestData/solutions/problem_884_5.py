class Solution:
	def solution_884_5(self, mat: List[List[int]], k: int) -> List[int]:
		helper = {}
		for index, row in enumerate(mat):
			helper[index] = 0
			for num in row:
				if num: helper[index] += 1
				else: break
		ans = sorted(helper, key = helper.get)
		return ans[:k]