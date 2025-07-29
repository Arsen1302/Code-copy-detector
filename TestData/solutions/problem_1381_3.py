class Solution:
    def solution_1381_3(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        q = []

        for i in range(0, len(original), n):
            q.append(original[i:i+n])
            
        return q