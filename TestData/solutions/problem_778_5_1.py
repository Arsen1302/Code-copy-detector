class Solution:
	def solution_778_5_1(self, s: str) -> str:
		i,j,k,n = 0,1,0,len(s)
		while j+k<n:
			if s[i+k]==s[j+k]:
				k+=1
				continue
			elif s[i+k]>s[j+k]:
				j+=k+1
			else:
				i=max(j,i+k+1)
				j=i+1
			k=0
		return s[i:]


	def solution_778_5_2(self, s: str) -> str:
		if len(s)<=1: return s
		i,res=1,set()
		while i<len(s)+1:
			for j in range(len(s)):
				if len(s[j:])<i:
					break
				res.add(s[j:j+i])
			i+=1
		res = sorted(res)
		return res[-1]