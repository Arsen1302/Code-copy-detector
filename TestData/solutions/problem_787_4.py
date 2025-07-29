class Solution(object):
    def solution_787_4(self, arr):
        arrLen = len(arr)
        prevMaxSub = arr[0]
        prevMaxSubWithDeletion = arr[0]
        maxSubWithDel = prevMaxSubWithDeletion
        
        for i in range(1, arrLen):
            newMaxSub = max(arr[i] + prevMaxSub, arr[i])
            prevMaxSubWithDeletion = max(prevMaxSubWithDeletion + arr[i],  newMaxSub, prevMaxSub)
            maxSubWithDel = max(maxSubWithDel, prevMaxSubWithDeletion)
            prevMaxSub = newMaxSub
            
        return maxSubWithDel
        
        """
        :type arr: List[int]
        :rtype: int
        """