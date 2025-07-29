class Solution:
    def solution_1348_2(self, word: str) -> int:
        count = 0
        ini = 'a'
        for i in word:
            x = abs(ord(i) - ord(ini))
            count += min(x, 26-x) + 1
            ini = i
        return count