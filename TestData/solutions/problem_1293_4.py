class Solution:
    def solution_1293_4(self, words: List[str]) -> bool:
        freq = defaultdict(int)
        for word in words: 
            for ch in word: freq[ord(ch)-97] += 1
        return all(x % len(words) == 0 for x in freq.values())