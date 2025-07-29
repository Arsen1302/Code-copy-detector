class Solution:
    def solution_1001_2(self, salary: List[int]) -> float:
        salary = sorted(salary)[1:len(salary)-1]
        return sum(salary) / len(salary)