class Solution:
    def solution_704_4(self, clips: List[List[int]], time: int) -> int:
        # Swipe Line
        clips.sort()
        if clips[0][0] != 0: return -1
        intervals = [(clips[0][0], clips[0][1])]
        for c in clips[1:]:
            l, r = c
            if intervals[-1][1] < l: break
            if intervals[-1][1] < r:
                while intervals and intervals[-1][0] >= l:  intervals.pop()
                if not intervals: intervals.append((l, r))
                elif intervals[-1][1] < r: intervals.append((intervals[-1][1], r))
        ret = 0
        for intv in intervals:
            ret += 1
            if time <= intv[-1]: return ret
        return -1
        # DP
        clips.sort()
        dp = [0] + [sys.maxsize] * time
        clips = sorted(clips)
        for clip in clips:
            s, e = clip[0], clip[1]
            for j in range(s, min(e, time)):
                dp[j+1] = min(dp[j+1], dp[s] + 1)
        return -1 if dp[-1] == sys.maxsize else dp[-1]