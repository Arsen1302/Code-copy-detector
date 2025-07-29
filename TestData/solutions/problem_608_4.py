class Solution:
    def solution_608_4(self, s: str) -> int:
        minFlips = flips = s.count('0')

        for c in s:
            if c == '0':
                flips -= 1
            else:
                flips += 1
            minFlips = min(minFlips, flips)
        
        return minFlips