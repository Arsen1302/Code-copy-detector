class Solution(object):
    def solution_540_3(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #binary search
        
        lower = 0
        upper = len(arr)-1
        
        while lower <= upper:
            mid = (lower+upper)//2
            print(arr[mid])
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            
            elif arr[mid-1] < arr[mid] < arr[mid+1]: # we are at the left side of the mountain we need to climb up to the right
                lower = mid+1
            elif arr[mid-1] > arr[mid] > arr[mid+1]: # we are at the right side of the mountain we need to climb up to the left
                upper = mid-1