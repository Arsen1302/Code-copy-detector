class Solution:
    def solution_542_4_1(self, s1: str, s2: str) -> int:
        n = len(s1)
        arr, s2_arr = list(s1), list(s2)
        min_steps = float('inf')
        
        def solution_542_4_2(steps,i):
            nonlocal min_steps
            if steps >= min_steps: return
			
            if i == n:
                min_steps = min(min_steps, steps)
                return
				
			# if character at index i is already correct
            if arr[i] == s2[i]:
                solution_542_4_2(steps,i+1)
                return
                
            for j in range(i+1,n):
				'''
				skip if:
					1. characters at i and j are the same
					2. character at j is not what we need at i
					3. character at j is already correctly placed
				'''
                if arr[i] == arr[j] or arr[j] != s2[i] or arr[j] == s2[j]: continue
                    
                arr[i], arr[j] = arr[j], arr[i]
                solution_542_4_2(steps+1,i+1)
                arr[i], arr[j] = arr[j], arr[i]
  
        solution_542_4_2(0,0) 
        return min_steps