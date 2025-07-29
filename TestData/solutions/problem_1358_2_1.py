class Solution:
    def solution_1358_2_1(self, tasks: List[int], sessionTime: int) -> int:
        tasks = sorted(tasks)

        @lru_cache(None)
        def solution_1358_2_2(x,tasks):
            if len(tasks) == 0:
                return 1
            ans = 0
            result = []
            if tasks[0] > x:
                ans += 1  #on to the new session as can't fit anything in 
                x = sessionTime #resets remaining session time to full session 
            for i,val in enumerate(tasks):
                if val <= x:
                    result.append(solution_1358_2_2(x-val,tasks[0:i] + tasks[i+1:]))
                else:
                    break
            return ans + min(result)
        
        return solution_1358_2_2(sessionTime,tuple(tasks))