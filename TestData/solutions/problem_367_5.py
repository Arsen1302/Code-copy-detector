class Solution:
    def solution_367_5(self, n: int, logs: List[str]) -> List[int]:
	    # Store total time of fid
        res = [0 for _ in range(n)]
		# stack
        s = []
		# store the current time
        currt = 0
		
		# iterate through the logs
        for log in logs: 
                
			# Get thefid , state and timestamp from the log	
            fid, state, timestamp = log.split(":")
            
            fid = int(fid)
            timestamp = int(timestamp)
            
            if state == "end":
				# since the process is ended, we pop out its start log
                s.pop()
				# Update the time of the log. We add **+1** as the process gets over at the end of timestamp. 
				# So adding that **1**
                res[fid] += timestamp - currt+1
				# updating the current time
                currt = timestamp + 1
            else:
                if (s):
				     # if another process is strating before the previious process has been ended, 
					 # we get the fid anf time of previouse proces
                    fidprev,time = s[-1]
					# add the time taken by previouse process till now before a new process is spawned
                    res[fidprev] += timestamp - currt
				# add the start log to the stack 
                s.append((fid,timestamp))
				# update the current time
                currt = timestamp
            
        return res