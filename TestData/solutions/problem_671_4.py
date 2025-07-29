class Solution:
    def solution_671_4(self, startValue: int, target: int) -> int:
        tempTarget = target
        tempStartValue = startValue
        
        ct1_p1 = 0
        while tempTarget > startValue:
            if tempTarget%2 == 0:
                tempTarget = tempTarget//2
            else:
                tempTarget += 1
            ct1_p1 += 1
            
        ct1_p2 = (startValue - tempTarget)
        
        
        ct2_p1 = 0
        while tempStartValue < target:
            tempStartValue = tempStartValue*2
            ct2_p1 += 1
        
        ct2_p2 = (tempStartValue - target)
        
        return min( ct1_p1+ ct1_p2, ct2_p1+ ct2_p2)