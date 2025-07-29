class Solution:
    def solution_511_4(self, A: List[int]) -> int:
        cnt = {}
        for x in sorted(A): 
            cnt[x] = 1 + sum(cnt[xx]*cnt[x//xx] for xx in cnt if not x%xx and x//xx in cnt)
        return sum(cnt.values()) % 1_000_000_007