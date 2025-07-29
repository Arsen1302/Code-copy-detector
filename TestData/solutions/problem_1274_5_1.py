class Solution:
    def solution_1274_5_1(self, s, i):
        if i < 0 or i >= len(s) or s[i] != '0':
            return
        if i == len(s)-1:
            self.ans = True
            return
        for jump in range(self.low, self.high+1):
            self.solution_1274_5_1(s, i+jump)
        
    def solution_1274_5_2(self, s: str, minJump: int, maxJump: int) -> bool:
        self.low = minJump
        self.high = maxJump
        self.ans = False
        self.solution_1274_5_1(s, 0)
        return self.ans