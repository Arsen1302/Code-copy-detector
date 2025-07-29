class Solution:
	def solution_509_4(self, s: str, c: str) -> List[int]:
		n = lastC =len(s)
		ans = [n] * n
		for i in itertools.chain(range(n), range(n)[::-1]):
			if s[i] == c: lastC = i
			ans[i] = min(ans[i], abs( i - lastC))
		return ans