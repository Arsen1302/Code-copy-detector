class Solution:
    def solution_901_5(self, date1, date2):
        a = date(*map(int, date1.split("-")))
        b = date(*map(int, date2.split("-")))
        return abs((a - b).days)