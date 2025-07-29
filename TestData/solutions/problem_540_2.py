class Solution(object):
    def solution_540_2(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        Brute force
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
                return i