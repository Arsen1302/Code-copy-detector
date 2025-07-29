class Solution:
    def solution_1001_4(self, salary: List[int]) -> float:
        salary.sort()
        salary = salary[1:-1]
        return sum(salary)/(len(salary))