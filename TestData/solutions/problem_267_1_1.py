class Solution:
    def solution_267_1_1(self, arr: List[int]) -> bool:
		# no way to make the square if total length not divisble by 4
        if sum(arr) % 4:
            return False
        
		# target side length
        side = sum(arr) // 4
        
        @lru_cache(None)
        def solution_267_1_2(k, mask, s):
			# finish all four sides
            if k == 4:
                return True
			# move on to next side if current one finished
            if not s:
                return solution_267_1_2(k+1, mask, side)
            
            for i in range(len(arr)):
				# if current matchstick used or longer than remaining side length to fill then skip
                if mask &amp; (1 << i) or s < arr[i]: continue
                if solution_267_1_2(k, mask ^ (1 << i), s - arr[i]):
                    return True
            return False
        
        return solution_267_1_2(0, 0, side)