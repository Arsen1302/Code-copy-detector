class Solution:
    def solution_318_2_1(self, timePoints: List[str]) -> int:
        def solution_318_2_2(t):
            return 60*int(t[:2]) + int(t[3:])
        
        maxMins = 60*24 # number of mins in a day
        if len(timePoints) > maxMins:
            return 0
    
        # we sort the timestamps. Idea: The smallest difference will always be a 
        # difference between two neighboring times in the array.
        ts = [solution_318_2_2(t) for t in timePoints]
        ts.sort()
        
        diffMin = maxMins
        # calculate the pairwise difference ...
        for i in range(1,len(ts)):
            t_high = ts[i]
            t_low = ts[i-1]
            diffMin = min(diffMin, t_high - t_low)
        # ... and due to the 24 hour clock, don't forget the last and first entry with modulo arithmetic
        diffMin = min(diffMin, (ts[0] - ts[-1]) % maxMins)
        
        return diffMin