class Solution:
    def solution_537_5(self, seats: List[int]) -> int:
        n = len(seats)
        MAX = 10 ** 9
        prefix = [MAX] * n
        suffix = [MAX] * n
        
        for i in range(n):
            if seats[i] == 1:
                prefix[i] = 0
            elif i > 0 and prefix[i - 1] != MAX:
                prefix[i] = 1 + prefix[i - 1]
        
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                suffix[i] = 0
            elif i < n - 1 and suffix[i + 1] != MAX:
                suffix[i] = 1 + suffix[i + 1]
        
        ans = 0
        for i in range(n):
            ans = max(ans, min(prefix[i], suffix[i]))
        
        return ans