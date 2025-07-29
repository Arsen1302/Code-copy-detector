class Solution:
    def solution_1685_5_1(self, s: str) -> int:
        @cache
        def solution_1685_5_2(s, i):
            if i == len(s):
                return 0
            ret = 1
            span = 1
            while i + span * 2 <= len(s):
                if s[i:i+span] == s[i+span:i+span*2]:
                    ret = max(ret, 1 + solution_1685_5_2(s, i + span))
                span += 1
            return ret
        ans = solution_1685_5_2(s, 0)
        solution_1685_5_2.cache_clear()
        return ans