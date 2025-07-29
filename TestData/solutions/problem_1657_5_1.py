class Solution:
	def solution_1657_5_1(self, mat: List[List[int]], cols: int) -> int:
		allCombinations = []

		def solution_1657_5_2(nums, k, path):
			if len(path) == k:
				allCombinations.append((path))
				return
			for i in range(len(nums)):
				solution_1657_5_2(nums[i+1:], k, path+[nums[i]])

		col = len(mat[0])
		ans = 0
		solution_1657_5_2(list(range(0, col)), cols, [])
		for comb in allCombinations:
			tot = 0
			comb = set(comb)
			for row in mat:
				flag = True
				for i in range(col):
					if row[i] and i not in comb:
						flag = False
						break
				if flag:
					tot += 1
			ans = max(ans, tot)
		return ans