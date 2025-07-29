class Solution:
    def solution_786_3(self, d: int, m: int, y: int) -> str:
        day=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
        if (m < 3) :
            y = y - 1
        return day[((y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7)]