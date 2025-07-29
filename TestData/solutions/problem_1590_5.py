class Solution:
    def solution_1590_5(self, brackets: List[List[int]], income: int) -> float:
        total_tax = 0
        prev = 0
        for i in range(len(brackets)):
            if income > brackets[i][0]:
                total_tax += (brackets[i][0] - prev) * brackets[i][1]
                prev = brackets[i][0]
            else:
                total_tax += (income - prev) * brackets[i][1]
                break
            
        return total_tax/100