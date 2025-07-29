class Solution:
    def solution_219_4(self, s: str) -> int:
        s = Counter(s)
        e = 0
        ss = 0
        for i in s.values():
            if i%2==0:
                ss+=i
            else:
                ss += i-1
                if e==0:
                    e=1
        return ss + e