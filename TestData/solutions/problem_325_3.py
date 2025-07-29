class Solution:
    def solution_325_3(self, s: str) -> bool:
        absent = late = 0 
        for i, ch in enumerate(s): 
            if ch == "A": absent += 1
            elif ch == "L": 
                if i == 0 or s[i-1] != "L": cnt = 0 
                cnt += 1
                late = max(late, cnt)
        return absent < 2 and late < 3