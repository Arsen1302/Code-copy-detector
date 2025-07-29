class Solution:
	def solution_140_4(self, nums: List[int]) -> None:

		p,q=0,0
		while q<len(nums):
			if nums[q]==0:
				q=q+1
			else:
				nums[p],nums[q]=nums[q],nums[p]
				p=p+1
				q=q+1

		return nums