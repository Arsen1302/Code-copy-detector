class Solution:
    def solution_1302_4(self, nums: List[int]) -> bool:
        dnums=nums.copy() #make a copy of the original array <nums>
        for i in range(len(nums)-1): #traverse the first pointer <i> in the original array <nums>
            if nums[i]>=nums[i+1]:
                a=nums.pop(i)
                break
        if nums==sorted(set(nums)):  #we are checking with the sorted array because there might be duplicate elements after 1 pop instruction
            return True
        for j in range(len(dnums)-1,0,-1): #traverse the 2nd pointer <j> in the duplicate array <dnums>
            if dnums[j]<=dnums[j-1]:
                a=dnums.pop(j)
                break
        if dnums==sorted(set(dnums)): 
            return True
        return False