class Solution:

	def solution_253_5(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

		d = {}
		res = 0

		for i in nums1:
			for j in nums2:
				temp = i + j
				try:
					d[temp] += 1
				except:
					d[temp] = 1

		for k in nums3:
			for l in nums4:
				temp = -(k + l)

				try:
					res += d[temp]
				except:
					pass

		return res