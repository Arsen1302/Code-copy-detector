class Solution:
    def solution_901_1_1(self, date1: str, date2: str) -> int:
        
        def solution_901_1_2(date): # calculates days passed since '1900-01-01'
            year0 = '1900'
            year1, month1, day1 = date.split('-')
                        
            days = 0
            for y in range(int(year0), int(year1)):
                days += 365
                if y%100 == 0:
                    if y%400 == 0:
                        days += 1
                else:
                    if y%4 == 0:
                        days += 1
                        
            for m in range(int(month1)):
                if m in [1, 3, 5, 7, 8, 10, 12]:
                    days += 31
                if m in [4, 6, 9, 11]:
                    days += 30
                if m == 2:
                    days += 28
                    if int(year1)%100 == 0:
                        if int(year1)%400 == 0:
                            days += 1
                    else:
                        if int(year1)%4 ==0:
                            days += 1
            days += int(day1)
            return days
			
        return abs(solution_901_1_2(date1) - solution_901_1_2(date2))