class Solution:
    def solution_1389_5(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        countMap = {}
        
        for i in set(nums1):
            countMap[i] = 1 + countMap.get(i, 0)
        
        for i in set(nums2):
            countMap[i] = 1 + countMap.get(i, 0)
        
        for i in set(nums3):
            countMap[i] = 1 + countMap.get(i, 0)
            
        res = []
        
        for i in countMap:
            if countMap[i] >= 2:
                res.append(i)
                
        return res