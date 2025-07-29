class Solution(object):
	def solution_1600_4(self, nums):
		#approach1
#         lis=[0 for _ in range(32)]
#         for i in range(32):
#             for j in nums:
#                 if 1<<i &amp; j:
#                     lis[i]=1
#                     break
#         s=0
#         val=1

#         for i in range(32):
#             if lis[i]:
#                 s+=val
#             val*=2
#         return s

#approach2
#as we know we have to find the xor of all the elements
#so we can observe there that we are calculating the sum only(of the odd bits)
#lets take example
#[3,2,4,6]
#3-0011
#2-0010
#4-0100
#6-0110
#so we have to find only odd bit sum
#so we make the 6th 3rd bit 0 to make the odd bit at the 3rd position
#and we know that if there exist 1 in any number at that position then we can make others 0 and take the first one to make the odd
#so here we are taking the or (which will take only the set bits - as we know 0 or 0 means 0 and 1 for all other cases)
		r = 0
		for num in nums:
			r |= num
		return r

		"""
		:type nums: List[int]
		:rtype: int
		"""