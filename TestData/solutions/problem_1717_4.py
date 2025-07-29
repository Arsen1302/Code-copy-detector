class Solution:
    def solution_1717_4(self, s: str, limit: int) -> List[str]:
        if limit <= 4: return []
        n = len(s)
        ans, step = float('inf'), 1
        while True:
            if 2 * len(str(step)) + 3 > limit: break
            lo, hi, suffix = step, min(n, step * 10 - 1), len(str(step)) + 3
            while lo <= hi:
                mid = (lo + hi) // 2
                idx, i  = 1, 0
                while i < n:
                    i += limit - (suffix + len(str(idx)))
                    idx += 1
                    if idx - 1 > mid: break
                idx -= 1
                if idx <= mid:
                    ans = min(ans, mid)
                    hi = mid - 1
                else: lo = mid + 1
            if ans != float('inf'): break
            step *= 10
        if ans == float('inf'): return []
        ans_split = []
        idx, i, suffix = 1, 0, len(str(ans)) + 3
        while i < n:
            ans_split.append(s[i:i + limit - (suffix + len(str(idx)))] + '<' + str(idx) + '/' + str(ans) + '>')
            i += limit - (suffix + len(str(idx)))
            idx += 1
        return ans_split