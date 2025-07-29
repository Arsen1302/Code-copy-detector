class Solution:
    def solution_704_5(self, clips: List[List[int]], T: int) -> int:
        from collections import defaultdict
        clip_map = defaultdict(list)
        clips.sort()
        for i, (s_i, e_i) in enumerate(clips):
            for s_j, e_j in clips[:i] + clips[i + 1:]:
                if s_i < s_j <= e_i and e_j > e_i:
                    clip_map[(s_i, e_i)].append((s_j, e_j))

        res = float('inf')
        for c in clips:
            q, path = [], 1
            if c[0] != 0: continue
            if c[1] >= T: return 1
            q = clip_map[tuple(c)]
            while q:
                s, e = q.pop()
                path += 1
                if e >= T:
                    break
                q += clip_map[(s, e)]
            else:
                path = float('inf')
            res = min(res, path)
        return -1 if res == float('inf') else res