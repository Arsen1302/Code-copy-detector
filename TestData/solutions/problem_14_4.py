class Solution:
	def solution_14_4(self, lst: List[str]) -> str:
		ans = ""
		for i in zip(*lst):
			p = "".join(i)
			if len(set(p)) != 1:
				return (ans)

			else:
				ans += p[0]

		return (ans)