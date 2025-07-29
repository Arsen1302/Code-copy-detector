class Solution:
    def solution_1485_4(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        m, s = divmod(targetSeconds, 60)
        cands = []
        if m < 100: cands.append((str(m) + str(s).zfill(2)).lstrip('0'))
        if m and s+60 < 100: cands.append((str(m-1) + str(s+60).zfill(2)).lstrip('0'))
        ans = inf 
        for cand in cands: 
            cost = 0
            prev = str(startAt)
            for ch in cand: 
                if prev != ch: cost += moveCost
                prev = ch
                cost += pushCost
            ans = min(ans, cost)
        return ans