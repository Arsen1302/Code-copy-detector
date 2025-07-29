class Solution:
    def solution_1628_2(self, grades: List[int]) -> int:
        
        sortedGrades = sorted(grades)

        groupNums = 0
        total = 0
        while total <= len(sortedGrades):
            groupNums += 1
            total += groupNums
        return groupNums - 1