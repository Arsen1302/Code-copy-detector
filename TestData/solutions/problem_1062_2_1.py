class Solution:
    def solution_1062_2_1(self, s: str) -> int:
        total = s.count('1')
        if total % 3: return 0
        avg = total // 3
        n, ans = len(s), 0
        @lru_cache(maxsize=None)
        def solution_1062_2_2(s, idx, part):
            nonlocal avg, n
            if part == 4 and idx == n: return 1
            cnt = cur = 0
            for i in range(idx, n):
                if s[i] == '1': cnt += 1
                if cnt == avg: cur += solution_1062_2_2(s, i+1, part+1)    
                elif cnt > avg: break 
            return cur
        return solution_1062_2_2(s, 0, 1) % 1000000007