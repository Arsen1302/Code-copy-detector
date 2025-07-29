class Solution:
    def solution_1009_4(self, arr: List[int]) -> bool:
        arr.sort()
        i = 0
        j = 1
        m = arr[j] - arr[i]
        while(j < len(arr)-1):
            if(arr[j+1]-arr[i+1] != m):
                return False
            i += 1
            j += 1
        return True