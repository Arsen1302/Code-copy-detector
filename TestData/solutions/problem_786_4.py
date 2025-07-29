class Solution:
    def solution_786_4(self, day: int, month: int, year: int) -> str:
        import time
        day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return day_of_week[time.strptime(f'{day} {month} {year}', '%d %m %Y')[6]]