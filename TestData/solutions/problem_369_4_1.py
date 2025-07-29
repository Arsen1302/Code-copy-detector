class Solution:
    def solution_369_4_1(self, price: List[int], special: List[List[int]], initial_needs: List[int]) -> int:
        memo = {}
        def solution_369_4_2(needs):
            lookup = str(needs)
            if lookup in memo: return memo[lookup]
            min_price = sum([price[idx]*needs[idx] for idx in range(len(needs))])
            
            for offer in special:
                if all([offer[i] <= needs[i] for i in range(len(needs))]):
                    updated_needs = [needs[i] - offer[i] for i in range(len(needs))]
                    min_price = min(min_price, offer[~0] + solution_369_4_2(updated_needs))
                    
            memo[str(needs)] = min_price
            return min_price
        
        return solution_369_4_2(initial_needs)