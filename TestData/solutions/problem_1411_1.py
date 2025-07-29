class Solution:
    def solution_1411_1(self, word: str) -> int:
        ans = 0 
        freq = defaultdict(int)
        for i, x in enumerate(word): 
            if x in "aeiou": 
                if not i or word[i-1] not in "aeiou": 
                    jj = j = i # set anchor
                    freq.clear()
                freq[x] += 1
                while len(freq) == 5 and all(freq.values()): 
                    freq[word[j]] -= 1
                    j += 1
                ans += j - jj
        return ans