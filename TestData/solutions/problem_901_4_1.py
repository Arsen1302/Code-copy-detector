class Solution:
    def solution_901_4_1(self, date1, date2):
        return abs(self.solution_901_4_2(date1) - self.solution_901_4_2(date2))
    
    def solution_901_4_2(self, date):
        y, m, d = map(int, date.split("-"))
        monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        extraDay = int(m > 2 and self.solution_901_4_3(y))
        
        days = 0
        days += sum(map(self.solution_901_4_4, range(1971, y)))
        days += sum(monthsDays[:m-1])
        days += d + extraDay
        
        return days

    def solution_901_4_3(self, y):
        return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
    
    def solution_901_4_4(self, y):
        return 365 + self.solution_901_4_3(y)