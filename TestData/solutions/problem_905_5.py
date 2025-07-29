class Solution:
    def solution_905_5(self, nums: List[int]) -> List[int]:
        
        nums1 = sorted(nums)                     #time O(nlogn)
        dic = {}
        answer = []
        
        for index,value in enumerate(nums1):     #time O(n)
            dic.setdefault(value,index)
                
        for i in nums:                           #time O(n)
            answer.append(dic[i])
            
        return answer
    
#time O(nlogn)
#space O(n)