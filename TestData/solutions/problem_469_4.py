**class Solution:
	def solution_469_4(self, n: int, k: int) -> int:
		if n==1 or k==1:
			return 0
		length=1<<n-1                         #2(n-1)
		mid=length//2
		if k<=mid:
			return self.solution_469_4(n-1,k)
		else:
			return (int (not(self.solution_469_4(n-1,k-mid))))**