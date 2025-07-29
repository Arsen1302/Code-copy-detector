# Approach 1: Brute Force Solution
# Time: O(mn)
# Space: O(n+m)
class Solution:
	def solution_895_2(self, grid: List[List[int]]) -> int:
		return sum([1 for i in grid for j in i if j < 0])

# Approach 2: Optimal Solution
# Time: O(n + m)
# Space: O(1)
class Solution:
	def solution_895_2(self, grid: List[List[int]]) -> int:
		n = len(grid[0])  # O(n)
		row = len(grid)-1  # O(m)
		clmn = 0
		cnt_neg = 0
		while row >= 0 and clmn < n:  # O(n) + O(m)
			if grid[row][clmn] < 0:
				cnt_neg += n-clmn
				row -= 1
			else:
				clmn += 1
		return cnt_neg