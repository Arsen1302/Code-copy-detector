class Solution:
	def solution_1368_4_1(self, s: str) -> int:
		def solution_1368_4_2(v):
			res=[]
			for i in range(n):
				if 1<<i&amp;v:
					res.append(s[i])
			if res==res[::-1]:
				pal[v]=len(res)
		pal=dict()
		n=len(s)
		for i in range(1,pow(2,n)):
			solution_1368_4_2(i)
		res=0
		for x in pal:
			for y in pal:
				if not x&amp;y:
					res=max(res,pal[x]*pal[y])
		return res