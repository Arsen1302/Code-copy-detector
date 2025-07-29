class Solution:
    def solution_883_1_1(self, jobDifficulty: List[int], d: int) -> int:
        jobCount = len(jobDifficulty)    
        if jobCount < d:
            return -1

        @lru_cache(None)
        def solution_883_1_2(jobIndex: int, remainDayCount: int) -> int:
            remainJobCount = jobCount - jobIndex
            if remainDayCount == 1:
                return max(jobDifficulty[jobIndex:])
            
            if remainJobCount == remainDayCount:
                return sum(jobDifficulty[jobIndex:])

            minDiff = float('inf')
            maxToday = 0
            for i in range(jobIndex, jobCount - remainDayCount + 1):
                maxToday = max(maxToday, jobDifficulty[i])
                minDiff = min(minDiff, maxToday + solution_883_1_2(i+1, remainDayCount-1))
            return minDiff

        return solution_883_1_2(0, d)