class Solution:
    def solution_1255_4(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0]!= 1:
            arr[0] = 1
        
        maxi = arr[0]
        print(arr)
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])>1:
                arr[i] = arr[i-1] +1
             
            maxi = max(maxi,arr[i])
        
        print(arr)
            
        
        return maxi