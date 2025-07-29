class Solution:
	def solution_780_1_1(self, queries: List[str], words: List[str]) -> List[int]:
		def solution_780_1_2(s):
			t = sorted(list(s))[0]
			return s.count(t)
		query = [solution_780_1_2(x) for x in queries]
		word = [solution_780_1_2(x) for x in words]
		m = []
		for x in query:
			count = 0
			for y in word:
				if y>x:
					count+=1
			m.append(count)
		return m