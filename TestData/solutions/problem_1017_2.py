class Solution:
	def solution_1017_2(self, nums: List[int]) -> int:
		nums, memo = sorted(nums), {} # sort to get the total number of digits that have duplicates
		for i in range(len(nums)-1): # lets say nums = [1,1,1,1,2,2,2,3] the total digits with duplicates is 7
			if nums[i] == nums[i+1]: # because nums has 4 ones and 3 twos so it adds up to 7
				if nums[i] not in memo: # 3 is not counted because there are no duplicates of it
					memo[nums[i]] = 1
				memo[nums[i]] = memo[nums[i]] + 1 
		# nums = [1,1,1,1,2,2,2,3]
		# so now memo = {1 : 4, 2: 3} which means we have 4 ones and 3 twos
		answer = 0
		for n in memo.values(): # this is the hard part, please refer to my beautiful drawing to understand this
			answer += (n**2 - n)//2 # after looking at the drawing, we repeat with each n value in memo

		return answer