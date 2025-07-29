class Solution:
    def solution_883_5_1(self, jobDifficulties: List[int], days: int) -> int:
        n = len(jobDifficulties)
        
        @cache
        def solution_883_5_2(i: int, days: int) -> int:
            if days == 0 or n - i < days:
                return -1
                
            if days == 1:
                # we can't partition any more
                return max(jobDifficulties[i:])
            
            res = math.inf
            
            curr_max = -math.inf
            for j in range(i, n - days + 1):
                # keep track of max in current "day"
                curr_max = max(curr_max, jobDifficulties[j])
                
                # keep track of min difficulty seen
                res = min(res, curr_max + solution_883_5_2(j + 1, days - 1))
            
            return res
        
        return solution_883_5_2(0, days)