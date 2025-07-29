class Solution:
	res = 0 
	def solution_816_2_1(self,arr):
		self.solution_816_2_2(arr,0,"")
		return self.res

	def solution_816_2_2(self,arr,ind,local):
		if len(local)!=len(set(local)):
			return
			
		self.res = max(self.res,len(local))
		for i in range(ind,len(arr)):
			self.solution_816_2_2(arr,i+1,local+arr[i])