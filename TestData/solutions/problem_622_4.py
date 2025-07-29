class Solution:
    def solution_622_4(self, arr: List[int]) -> bool:
        decreasestarted= False
        #edge cases
        if (len(arr)< 3): return False
        if (arr[0]>arr[1]): return False
        
        for i in range(len(arr)-1):
            if (not decreasestarted):
                if (arr[i]>=arr[i+1]):
                    decreasestarted = True
            if (decreasestarted and arr[i]<=arr[i+1]):
                return False
            
        return True if decreasestarted   else False