class Solution:
    def solution_980_2(self, target: List[int], arr: List[int]) -> bool:
        
        return Counter(arr) == Counter(target)