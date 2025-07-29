class Solution:
	def solution_1086_5(self, nums: List[int]) -> int:
		freq=[0 for _ in range(max(nums)+1)]
		for i in nums:
			freq[i]+=1
		suff=[freq[-1]]
		for i in freq[::-1][1:]:
			suff.append(suff[-1]+i)
		suff=suff[::-1]
		for i in range(max(nums)+1):
			if suff[i]==i:
				return i
		return -1