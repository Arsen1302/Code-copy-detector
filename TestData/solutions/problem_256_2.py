class Solution:
    def solution_256_2(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            seen=set()
            while True:
                if i in seen:               # if index already exist in set means, array is circular 
                    return True
                seen.add(i)
                prev=i
                i=(i+nums[i])%len(nums)        # index position for next element
                if prev==i or (nums[i]>0)!=(nums[prev]>0):         # checks whether all the elements in circular subset have same sign
                    break       
        return False