class Solution:
    def solution_520_4(self, image: List[List[int]]) -> List[List[int]]:
        
        return [[0 if n else 1 for n in i] for i in [item[::-1] for item in image]]