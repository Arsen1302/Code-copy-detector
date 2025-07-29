class Solution:
    def solution_704_3(self, clips: List[List[int]], time: int) -> int:
        # first sort the clips
        clips.sort()
        # if start is not 0 we can never cover entire event
        if clips[0][0] != 0 : return -1
        # dictionary (key,value) key = int value = max int we can reach from value in 1 move
        dictionary = {}
        for x,y in clips:
            dictionary[x] = y
        # make a dp list
        dp = [float('inf')]*(time+1)
        dp[0] = 0
        for i in range(1,time+1):
            best = dp[i]
            for j in range(i):
                # can we reach i or above i from j
                if j in dictionary and dictionary[j] >= i:
                    # if yes can we reach in minimum steps so far
                    if dp[j] + 1 < best: best = dp[j] + 1
            if best == float('inf'):return -1
            dp[i] = best
        return dp[-1] if dp[-1] != float('inf') else -1