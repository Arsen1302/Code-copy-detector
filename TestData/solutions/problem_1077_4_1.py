class Solution:
	def solution_1077_4_1(self, s: str) -> int:
		ans = 0
		n = len(s)
		def solution_1077_4_2(index,current,vis):
			nonlocal ans,n
			if(index == n):
				ans = max(ans,current)
				return
			for i in range(index,n):
				# print(s[index:i])
				if(s[index:i+1] not in vis):
					solution_1077_4_2(i+1,current+1,vis+(s[index:i+1],))
		solution_1077_4_2(0,0,())
		return ans