class Solution:
    def solution_1090_2(self, s: str) -> int:
        r = cnt = 0
        for c in s:
            if c == ")":
                if cnt:
                    cnt -= 1
                    r = max(r, cnt + 1)
            elif c == "(":
                cnt += 1
                
        return r