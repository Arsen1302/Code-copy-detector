class Solution:
    def solution_230_2(self, s: str) -> str:
        # (z)ero, one, t(w)o, three, fo(u)r, five, si(x), seven, ei(g)ht, nine
        from collections import Counter
        sc = Counter(s)
        digits = {0: Counter("zero"), 1: Counter("one"), 2:Counter("two"), 3:Counter("three"), 4:Counter("four"), 5:Counter("five"), 6:Counter("six"), 7: Counter("seven"), 8: Counter("eight"), 9: Counter("nine")}
        counts = [0]*10
        
        for i in [0, 2, 4, 6, 8, 3, 1, 7, 5, 9]:
            digit = digits[i]
            while digit <= sc:
                sc -= digit
                counts[i] += 1
                
        return "".join([str(i)*c for i, c in enumerate(counts)])