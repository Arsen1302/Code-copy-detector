class Solution:
    def solution_1001_3(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary)/len(salary)