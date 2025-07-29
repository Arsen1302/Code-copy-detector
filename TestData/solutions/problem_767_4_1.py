class Solution:
    def solution_767_4_1(self, piles: List[int]) -> int:
        N = len(piles)
        self.dp = {}

        def solution_767_4_2(start, M):            
            if start >= N:
                return 0
            
            # take all if possible
            if N - start <= 2*M:
                return sum(piles[start:])
            
            # memoization
            if (start, M) in self.dp:
                return self.dp[(start, M)]

            my_score = 0
            total_score = sum(piles[start:])
            # the opponent can take [1, 2*M] stones
            for x in range(1, 2*M+1):
                # get opponent's score
                opponent_score = solution_767_4_2(start+x, max(x, M))
                # maintains max my_score
                my_score = max(my_score, total_score - opponent_score)
                
            self.dp[(start, M)] = my_score
                
            return my_score
        
        
        return solution_767_4_2(0, 1)