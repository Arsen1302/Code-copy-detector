class Solution:
	def solution_1484_1(self, nums: List[int], pivot: int) -> List[int]:

		ans=[]

		nums.remove(pivot)

		i=0
		ans.append(pivot)

		for j in nums:
			if j<pivot:
				ans.insert(i,j)
				i=i+1
			elif j==pivot:
				ans.insert(i+1,j)
			else:
				ans.append(j)

		return ans