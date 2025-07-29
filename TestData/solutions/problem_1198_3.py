class Solution:
    def solution_1198_3(self, groups: List[List[int]], nums: List[int]) -> bool:
        
        k=0                         
        found = 0
        j = 0
        
        # traverse the whole nums list, 
        ## if nums[k] is same as the value of 0'th index of a group
        ## check whether the subarray of nums starting at index k upto index k+len(group)-1 is same as group
        ## if so, increase k and found variables accordingly
        ## otherwise increment k
        while k<len(nums):
            if k==len(nums) or found==len(groups):          #reached the end of list nums or matched all the groups
                break
            if nums[k]==groups[j][0]:                       #as groups must be in nums in the given order, start checking from group at index 0
                if nums[k:k+len(groups[j])]==groups[j]:     #check whether the subarray matches the group
                    found+=1
                    k+=len(groups[j])                       #increase k by the length of the group
                    j+=1                                    #increment j
                else:
                    k+=1                                    #not matched, increment k
            else:
                k+=1                                        #nums[k] does not match leftmost value of group, increment k
                
        return found==len(groups)