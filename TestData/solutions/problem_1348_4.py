class Solution:
    def solution_1348_4(self, word: str) -> int:
        d = {chr(i):(i-97) for i in range(97, 123)}
        cur = 'a'
        ans = 0
        for w in word:
            offset = min(abs(d[w] - d[cur]), 26 - abs(d[w] - d[cur]))
            
            cur = w
            ans += offset + 1
        return ans