class Solution:
    def solution_850_2(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = {}
        temp = {}
        for i in range(len(s)): 
            temp[s[i]] =  1 + temp.get(s[i], 0)
            if i >= minSize: 
                temp[s[i-minSize]] -= 1 
                if temp[s[i-minSize]] == 0: temp.pop(s[i-minSize])
            
            if i >= minSize-1 and len(temp) <= maxLetters: 
                key = s[i-minSize+1: i+1]
                freq[key] = 1 + freq.get(key, 0)
        return max(freq.values(), default=0)