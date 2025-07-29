class Solution:
    def solution_1094_3(self, arr: List[int]) -> float:
        counter = 0.05*len(arr)
        
        while counter != 0:
            arr.remove(min(arr))
            arr.remove(max(arr))
            counter -= 1
            
        return sum(arr) / len(arr)