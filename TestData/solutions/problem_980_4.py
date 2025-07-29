class Solution:
    def solution_980_4(self, target: List[int], arr: List[int]) -> bool:
        for i in target:
            if target.count(i) != arr.count(i) :
                return False 
        return True