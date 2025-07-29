class Solution:
    def solution_103_1(self, k: int, n: int) -> List[List[int]]:
        
        current_combination, combinations = [], []
        integer, combination_sum = 1, 0
        queue = [(integer, current_combination, combination_sum)]
        while queue:
            integer, current_combination, combination_sum = queue.pop()
            if combination_sum == n and len(current_combination) == k: combinations.append(current_combination)
            else:
                for i in range(integer, 10):
                    if combination_sum + i > n: break
                    queue.append((i+1, current_combination + [i], combination_sum + i))
        
        return combinations