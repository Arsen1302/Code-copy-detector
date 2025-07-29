class Solution:
    def solution_935_1(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        solution_935_1 = dishSum = 0

        for dish in satisfaction:
            dishSum += dish
            if dishSum <= 0:
                break
            solution_935_1 += dishSum
        
        return solution_935_1