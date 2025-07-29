class Solution:
    def solution_905_3(self, nums: List[int]) -> List[int]:
        
        nums1 = sorted(nums)            #time O(nlogn)
        dic = {}
        answer = []
        
        for i in range(0,len(nums1)):   #time O(n)
            if nums1[i] in dic:         #time O(1)
                continue
            else:
                dic[nums1[i]] = i
                
        for i in range(0,len(nums)):    #time O(n)
            answer.append(dic[nums[i]])
            
        return answer
    
#time O(nlogn)
#space O(n)