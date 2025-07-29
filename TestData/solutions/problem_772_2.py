class Solution:
    def solution_772_2(self, date: str) -> int:
        year, month, day = date.split('-')
        
        year = int(year)
        month = int(month)
        day = int(day)
        
        isleapYear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        cnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if isleapYear:
            cnt[1] = cnt[1] + 1
        
        ans = 0
        for i in range(month-1):
            ans += cnt[i]
        
        return ans + day