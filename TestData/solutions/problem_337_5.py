class Solution:
    def solution_337_5(self, nums: List[int]) -> int:
        # you can use set to mark the element where you've been before but instead of extra memory you can just give the value of -1 to every element you've visited
        # then you just check if the current element is different from -1, if so you have to iterate in order to create a new path 
        # mark with -1 since the all elements are positive 
		#if you like it, please upvote! ^^
        
        count_max = 0
        for i in range(len(nums)):
            if nums[i] != -1: #if it's not visited 
                count = 0
                j = i
                while nums[j] != -1:
                    t = j
                    j = nums[j]
                    count += 1
                    nums[t] = -1 # marking
                if count > count_max:
                    count_max = count
        return count_max