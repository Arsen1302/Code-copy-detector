class Solution:
    def solution_1293_5(self, words: List[str]) -> bool:
        
        n = len(words)
        d = defaultdict(int)
        
        for word in words:
            for ch in word:
                d[ch] += 1
        
        for letter_count in d.values():
            if letter_count % n != 0:
                return False
            
        
        return True