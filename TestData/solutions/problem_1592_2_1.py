class Solution:
    def solution_1592_2_1(self, cookies: List[int], k: int) -> int:
        result = float('inf')
        children = [0] * k
        
        def solution_1592_2_2(index):
            nonlocal result, children
            
            if index == len(cookies):
                result = min(result, max(children))
                return
				
			# key point to pass the TLE!
            if result <= max(children):
                return
            
            for i in range(k):
                children[i] += cookies[index]
                solution_1592_2_2(index + 1)
                children[i] -= cookies[index]
                
        solution_1592_2_2(0)
        
        return result