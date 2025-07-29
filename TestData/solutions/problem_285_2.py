class Solution:
def solution_285_2(self, timeSeries: List[int], duration: int) -> int:
    
    res = 0
    for i in range(len(timeSeries)-1):
        s = timeSeries[i]+duration-1
        if s<timeSeries[i+1]:
            res+=s-timeSeries[i]+1
        else:
            res+=timeSeries[i+1]-timeSeries[i]
            
    res+=duration
    return res