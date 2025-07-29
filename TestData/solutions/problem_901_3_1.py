class Solution:
    def solution_901_3_1(self, date1: str, date2: str) -> int:
        
        # use a solution_901_3_2 func to find out how many days from the date to the base year (1971 as constraint)
        def solution_901_3_2(y,m,d):
            days = 0
            month_days = [31,28,31,30,31,30,31,31,30,31,30,31] # days in each month 
            
            days += (y - 1971) * 365 # assume no leap yaer 
            for _ in range(1972, y, 4): # now adding leap years, why 1972, becuze 1972 is the first leap year 
                days += 1
			# days += (y - 1971) // 4  >>>>>> I am not able ot find out a math way to calculate here, anyone help? . 
            
            days += sum(month_days[:m-1]) # Jun-20, 0-indexed month_days, hence m-1
            days += d
            
            # Tips: after google a bit about leap year calculate, 
            # year 300, 700, 1800 should div by 400, not 4 only. i was thought 4 is always for leap year... 
            if m > 2 and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
                days += 1
            
            return days 
        
        y1,m1,d1 = date1.split('-')
        y2,m2,d2 = date2.split('-')
        
        days1 = solution_901_3_2(int(y1), int(m1), int(d1))
        days2 = solution_901_3_2(int(y2), int(m2), int(d2))
        return abs(days1 - days2)