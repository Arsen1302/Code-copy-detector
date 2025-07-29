class Solution:
    # use two frequency counters.
    
    # O(n) time : O(26) = O(1) space
    def solution_1415_3(self, word1: str, word2: str) -> bool:
        freq1, freq2 = Counter(word1), Counter(word2)

        for c,f in freq1.items():
            if abs(f - freq2[c]) > 3: return False
        
        for c,f in freq2.items():
            if abs(f - freq1[c]) > 3: return False

        return True