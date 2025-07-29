class Solution:
	def solution_178_2(self, nums1: List[int], nums2: List[int]) -> List[int]:

		result = []

		for i in nums1:
			if i in nums2 and i not in result:
				result = result  + [i]*min(nums1.count(i),nums2.count(i))

		return result