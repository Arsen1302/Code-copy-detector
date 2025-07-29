class Solution:
    def solution_103_2_1(self, k: int, n: int) -> List[List[int]]:
        
        combinations = []
        counter = [(integer, 1) for integer in range(1, 10)]
        
        def solution_103_2_2(integer = 0, current_combination = [], combination_sum = 0):
            if combination_sum > n or len(current_combination) > k or integer not in range(9): return
            elif combination_sum == n and len(current_combination) == k: combinations.append(current_combination.copy())
            else:
                candidate, frequency = counter[integer]
                if frequency == 1:
                    counter[integer] = (candidate, 0)
                    solution_103_2_2(integer, current_combination + [candidate], combination_sum + candidate)
                counter[integer] = (candidate, frequency)
                solution_103_2_2(integer+1, current_combination, combination_sum)
                
        solution_103_2_2()
        return combinations