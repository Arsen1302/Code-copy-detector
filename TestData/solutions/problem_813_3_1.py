class Solution:
    def solution_813_3_1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()

        @lru_cache(None)
        def solution_813_3_2(i):
            if i == N: return 0
            j = i + 1
            while j < N and jobs[i][1] > jobs[j][0]:
                j += 1
            one = jobs[i][2] + solution_813_3_2(j)
            two = solution_813_3_2(i+1)
            return max(one, two)
        
        return solution_813_3_2(0)