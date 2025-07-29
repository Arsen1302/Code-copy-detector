class Solution:
	def solution_676_4_1(self, nums: List[int]) -> int:
		def solution_676_4_2(v):
			k=int(math.sqrt(v))
			return k*k==v
		nums.sort()
		def solution_676_4_3(A,prev):
			if len(A)==0:
				self.res+=1
				return 
			for j in range(len(A)):
				if j>0 and A[j]==A[j-1]:continue
				if prev is None:
					solution_676_4_3(A[:j]+A[j+1:],A[j])
				elif solution_676_4_2(prev+A[j]):
					solution_676_4_3(A[:j]+A[j+1:],A[j])
		self.res=0
		solution_676_4_3(nums,None)
		return self.res