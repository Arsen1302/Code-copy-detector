class Solution:
	def solution_1613_4(self, nums: List[int], threshold: int) -> int:
		l,n=[],len(nums)
		stack=[]
		for i,x in enumerate(nums):
			while stack and nums[stack[-1]]>=x:
				stack.pop()
			if stack:
				l.append(stack[-1])
			else:
				l.append(-1)
			stack.append(i)
		stack=[]
		for i in range(n-1,-1,-1):
			while stack and nums[stack[-1]]>=nums[i]:
				stack.pop()
			if stack:
				k=stack[-1]-l[i]-1
			else:
				k=n-l[i]-1
			if k*nums[i]>threshold:
				return k
			stack.append(i)
		return -1