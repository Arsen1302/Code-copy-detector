class Solution:
    def solution_899_3(self, s: str) -> int:
            
        HashMap = {c :0 for c in 'abc'}
        countS = 0
        r = 0
            
        for l in range(len(s)):
            while not all(HashMap.values()) and r < len(s):
                HashMap[s[r]] += 1
                r += 1
            
            if all(HashMap.values()):
                countS += len(s) - r +1
                HashMap[s[l]] -= 1
        return countS