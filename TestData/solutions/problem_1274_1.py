class Solution:
    def solution_1274_1(self, s: str, minJump: int, maxJump: int) -> bool:
        prefix = [0, 1]
        for i in range(1, len(s)): 
            prefix.append(prefix[-1])
            lo = max(0, i-maxJump)
            hi = max(0, i-minJump+1)
            if s[i] == "0" and prefix[hi] - prefix[lo] > 0: prefix[-1] += 1
        return prefix[-1] > prefix[-2]