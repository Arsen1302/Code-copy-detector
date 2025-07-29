class Solution:
    def solution_1323_2(self, s: str) -> bool:
        a = set(s)
        d = set()
        for i in a:
            d.add(s.count(i))
        if len(d) == 1:
            return True
        else:
            False