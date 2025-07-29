class Solution:
     def solution_913_3(self, n: int) -> str:
		# we can use any of the 2 alphabets of our choice
        return "v" * n if n % 2 else "v" * (n-1) + "m"