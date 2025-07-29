class Solution:
    def solution_1323_5(self, s: str) -> bool:
        a = []
        for i in s:
            a.append(s.count(i))
        print(a)
        if a.count(a[0]) == len(a):
            return True