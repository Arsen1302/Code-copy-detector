class Solution:
    def solution_190_5(self, nums: List[int]) -> int:
        #create 2 lists to capture positive and negative wiggle sequences
        pos = [1 for _ in range(len(nums))]
        neg = [1 for _ in range(len(nums))]
        
        for i in range(1,len(nums)):
            # if the current number is > previous, we add 1 to the last occurence of negative sequence
            # and store it as a positive sequence
            if nums[i]>nums[i-1]:
                pos[i] = neg[i-1]+1
                neg[i] = neg[i-1]
            # if the current number is < previous, we add 1 to the last occurence of positive sequence
            # and store it as a negative sequence
            elif nums[i]<nums[i-1]:
                neg[i] = pos[i-1]+1
                pos[i] = pos[i-1]
            # else we just keep copy the previous sequence until a positive or negative sequence occurs
            else:
                neg[i] = neg[i-1]
                pos[i] = pos[i-1]
        #max wiggle subsequence can either come from positive sequence or negative sequence
        return max(pos[-1],neg[-1])