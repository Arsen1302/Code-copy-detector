class Solution:
    def solution_1690_3_1(self, time: str) -> int:
        def solution_1690_3_2(value):
            if value < 10:
                return "0" + str(value)
            return str(value)
        
        def solution_1690_3_3(clock, pattern):
            s = solution_1690_3_2(clock)
            if pattern[0] != "?" and s[0] != pattern[0] or pattern[1] != "?" and s[1] != pattern[1]:
                return False
            return True
            
        
        hPattern, mPattern = time.split(":")
        ans = 0
        hhCnt, mmCnt = 0, 0
        for hh in range(24):
            if solution_1690_3_3(hh, hPattern):
                hhCnt += 1
        for mm in range(60):
             if solution_1690_3_3(mm, mPattern):
                mmCnt += 1
        return hhCnt * mmCnt