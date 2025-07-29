class Solution:
    def solution_786_2_1(self, day: int, month: int, year: int) -> str:
        
        def solution_786_2_2(y, m, d): 
            """Return year-month-day in number format."""
            if m < 3: 
                y -= 1
                m += 12
            return 365*y + y//4 - y//100 + y//400 + (153*m + 8)//5 + d
        
        weekday = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        return weekday[(solution_786_2_2(year, month, day) - solution_786_2_2(2021, 4, 11)) % 7]