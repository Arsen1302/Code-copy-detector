class Solution(object):
    def solution_285_1(self, timeSeries, duration):
        repeat = 0
        for i in range(len(timeSeries)-1):
            diff = timeSeries[i+1] - timeSeries[i]
            if diff < duration:
                repeat += duration - diff
        return len(timeSeries)*duration - repeat