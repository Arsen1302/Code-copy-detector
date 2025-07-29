class Solution:
    def solution_1671_3(self, n: int) -> int:
		# or simply check if it is divisable by 2, if so return n
		# else return its double
        return 2 * n if n &amp; 1 else n