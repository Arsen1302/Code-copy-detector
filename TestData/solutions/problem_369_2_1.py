class Solution:
    def solution_369_2_1(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        @lru_cache(None)
        def solution_369_2_2(*args): 
            """Return the lowest price one has to pay to get items in args."""
            ans = sum(x*y for x, y in zip(args, price))
            for offer in special: 
                if all(x >= y for x, y in zip(args, offer)):
                    ans = min(ans, solution_369_2_2(*(x-y for x, y in zip(args, offer))) + offer[-1])
            return ans 
            
        return solution_369_2_2(*needs)