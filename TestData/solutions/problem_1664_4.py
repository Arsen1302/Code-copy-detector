class Solution:
    def solution_1664_4(self, s: str) -> int:
        i, n, cnt = 0, len(s), 1
        seen = set()
        while i < n:
            #print(seen)
            if s[i] in seen:
                cnt += 1
                seen = set()
            seen.add(s[i])
            i += 1
        return cnt