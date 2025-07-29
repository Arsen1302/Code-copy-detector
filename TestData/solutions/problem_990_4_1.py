class Solution:
    def solution_990_4_1(self, houses: List[int], cost: List[List[int]], _: int, colors: int, target: int) -> int:
        
        @cache
        def solution_990_4_2(index, last_color, neighborhoods):
            if index == len(houses):
                return 0 if neighborhoods == target else float('inf')
            
            if neighborhoods > target:
                return float('inf')
            
            # this house needs to be painted
            if houses[index] == 0:
                result = float('inf')
                for c in range(1, colors + 1):
                    result = min(result, solution_990_4_2(index + 1, c, neighborhoods + (c != last_color)) + cost[index][c-1])
                return result
            
            # this house is already painted
            return solution_990_4_2(index + 1, houses[index], neighborhoods + (houses[index] != last_color))
        
        result = solution_990_4_2(0, 0, 0)
        return result if result != float('inf') else -1