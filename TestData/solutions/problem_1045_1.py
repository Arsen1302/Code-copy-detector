class Solution:
    def solution_1045_1(self, arr: List[int]) -> bool:
        count = 0
        
        for i in range(0, len(arr)):
            if arr[i] %2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False