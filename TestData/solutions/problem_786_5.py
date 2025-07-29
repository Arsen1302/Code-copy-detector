class Solution:
    def solution_786_5(self, day: int, month: int, year: int) -> str:
        week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        return week_days[date(year,month,day).weekday()]