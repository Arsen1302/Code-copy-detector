class Solution:
    def solution_767_5_1(self, piles):
        # accumulated sum table of the rest of all stores reversely for quick check
        a = [*accumulate(piles[::-1])][::-1]
		
        # dp cache 
        @lru_cache(None)
        def solution_767_5_2(i, m): 
		    # i: current index, m: current maximal move
            # if player's move can arrive goal, get all rest stones
            if i + 2 * m >= len(piles): return a[i]
            
            # otherwise, 
            # the rest of all stones must subtract rival's minimum  
            # _minScore: rival's minimum         
            _minScore = 2**31 - 1  

            # find which move can get maximum
            # x: how many moves
            for x in range(1, 2 * m + 1):
                # get rival's score
                score = solution_767_5_2(i + x, x) if x > m else solution_767_5_2(i + x, m)
                # update rival's new minimum 
                if score < _minScore: _minScore = score

            # the rest of all stores of current position
            # subtract rival's minimum to get best result
            return a[i] - _minScore
            
        return solution_767_5_2(0, 1)