class Solution:
    def solution_1358_3_1(self, tasks: List[int], sessionTime: int) -> int:
	
        # if sum fully divisible, the answer can be directly calculated
        total_tasks = sum(tasks)
        quotient, remainder = divmod(total_tasks, sessionTime)
        
        sessions = []
        ans = len(tasks)  # cant be more sessions so start with that
        least_num_sessions = quotient + (remainder > 0)  # incase of a non-zero remainder, this is the least number of sessions possible
        
        def solution_1358_3_2(idx):
            nonlocal ans
            if len(sessions) >= ans:
                return
            
            if idx == len(tasks):
                if ans == least_num_sessions:
                    return True  # cant be lower so stop searching
                ans = min(ans, len(sessions))
                return
            
            # check if this value fits in any of the existing sessions
            for i in range(len(sessions)):
                if sessions[i] + tasks[idx] <= sessionTime:
                    sessions[i] += tasks[idx]
                    if solution_1358_3_2(idx + 1):
                        return True
                    sessions[i] -= tasks[idx]
            
            # give value its own session
            sessions.append(tasks[idx])
            if solution_1358_3_2(idx + 1):
                return True
            sessions.pop()
        
        solution_1358_3_2(0)
        return ans