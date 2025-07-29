class Solution:
	def solution_823_3(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
		bm = [[0 for _ in range(len(colsum))] for i in range(2)]
		for i in range(len(colsum)):
			if colsum[i]==2:
				colsum[i]=0
				upper-=1
				lower-=1
				bm[0][i]=1
				bm[1][i]=1

		for i in range(len(colsum)):
			if colsum[i]>0 and upper>0:
				bm[0][i]=1
				upper-=1
				colsum[i]-=1
		for i in range(len(colsum)):
			if colsum[i]>0 and lower>0:
				bm[1][i]=1
				lower-=1
				colsum[i]-=1
		if upper!=0 or lower!=0 or sum(colsum)!=0:
			return []
		return bm