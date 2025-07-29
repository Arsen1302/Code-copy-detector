class Solution:
    def solution_1255_3(self, arr: List[int]) -> int:
        
        arr.sort()        
        
        c = 1
            
        for i in range(0 , len(arr)):
            if c <= arr[i]:
                c += 1
            
        return c - 1