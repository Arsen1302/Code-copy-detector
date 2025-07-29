class Solution:
    def solution_1533_4(self, current: str, correct: str) -> int:
        fn = lambda x, y: 60*x + y
        m0 = fn(*map(int, current.split(':')))
        m1 = fn(*map(int, correct.split(':')))
        ans = 0 
        diff = m1 - m0 
        for x in 60, 15, 5, 1: 
            ans += diff // x
            diff %= x
        return ans