class Solution:
	def solution_1220_3_1(self, nums: List[int], k: int) -> int:
		def solution_1220_3_2(arr):
			ans=[]
			stack=[]
			for i in range(len(arr)-1,-1,-1):
				while stack and arr[stack[-1]]>=arr[i]:
					stack.pop()
				if not stack:
					ans.append(len(arr))
				else:
					ans.append(stack[-1])
				stack.append(i)
			return ans[::-1]
		def solution_1220_3_3(arr):
			ans=[]
			stack=[]
			for i in range(len(arr)):
				while stack and arr[stack[-1]]>=arr[i]:
					stack.pop()
				if not stack:
					ans.append(-1)
				else:
					ans.append(stack[-1])
				stack.append(i)
			return ans
		nslArr= solution_1220_3_3(nums)
		nsrArr= solution_1220_3_2(nums)
		score =0
		#here we are finding the nearest smaller to the left and to the right 
		#because we want to maximize and for a number we find its minimum from both side and take +1 index from left and -1 index from the right
		#and for the range r-l-1 -
		#for the length it is r-l+1 but we are removing the l and r because these are the minimum so r-l+1-2 -> r-l-1
		for i in range(len(nums)):
			l = nslArr[i]
			r = nsrArr[i]
			if l+1<=k and r-1>=k:
				score=max(score,nums[i]*(r-l-1))
		return score