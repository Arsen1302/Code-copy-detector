class Solution:
	def solution_70_1(self, lst: List[int]) -> int:
		start, end = 0, len(lst) - 1

		while start < end:

			mid = start + (end - start) // 2

			if lst[mid] > lst[mid + 1]:
				end = mid
			else:
				start = mid + 1

		return start