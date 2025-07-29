class Solution:
	def solution_845_4(self, low: int, high: int) -> List[int]:

		ans=[]
		s='123456789'

		for i in range(len(s)-1):
			j=2
			while j<10:
				if int(s[i:i+j]) not in ans:
					if int(s[i:i+j]) in range(low,high+1):
						ans.append(int(s[i:i+j]))
				j=j+1

		ans.sort()
		return ans