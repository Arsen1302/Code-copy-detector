class Solution:
    def solution_445_5(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters)-1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if letters[mid] > target:
                end = mid - 1
            else :
                start = mid + 1
                
        return letters[start%len(letters)]