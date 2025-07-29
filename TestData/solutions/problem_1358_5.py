class Solution:
    def solution_1358_5(self, tasks: List[int], sessionTime: int) -> int:
        # dp[ntasks+1][sesstionTime+1]
		# Put large tasks first
        tasks.sort(reverse=True)
        
        tasks_ = [tasks[i] for i in range(len(tasks))]
        nSession = 0
        while len(tasks_) > 0:
            # Put as many task as possible into one session
            dp = [[0] * (sessionTime+1) for _ in range(len(tasks_)+1)]
            path = [[False] * (sessionTime+1) for _ in range(len(tasks_)+1)]
            
            delete = [False] * len(tasks_)
            nNew = len(tasks_)
            
            for i in range(1,len(tasks_)+1):
                for j in range(1,sessionTime+1):
                    dp[i][j] = dp[i-1][j]
                    if (j-tasks_[i-1] >= 0):
                        # Put in tasks[i-1]
                        if dp[i][j] < dp[i-1][j-tasks_[i-1]] + tasks_[i-1]:
                            dp[i][j] = dp[i-1][j-tasks_[i-1]] + tasks_[i-1]
                            path[i][j] = True
                            nNew -= 1

			# Remove those tasks in the current session            
            k = sessionTime;
            for i in range(len(tasks_), 0, -1):
                if path[i][k] and k >= 1:
                    delete[i-1] = True
                    k = k - tasks_[i-1]
                        
            newtasks_ = []
            count = 0
            for i in range(len(tasks_)):
                if not delete[i]:
                    newtasks_.append(tasks_[i])
        
            tasks_ = newtasks_
            
            nSession += 1
            
        return nSession