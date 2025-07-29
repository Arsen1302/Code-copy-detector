class Solution:
    def solution_367_3(self, n: int, logs: List[str]) -> List[int]:
        ftimes = [0] * n
        stack = []
        prev_start_time = 0
        
        for log in logs:
            fid, indicator, ftime = log.split(":")
            fid, ftime = int(fid), int(ftime)
            
            if indicator == 'start':
                if stack:
                    ftimes[stack[-1]] += ftime - prev_start_time
                    
                stack.append(fid)
                prev_start_time = ftime
                
            else:
                ftimes[stack.pop()] += ftime - prev_start_time + 1
                prev_start_time = ftime + 1
                
        return ftimes