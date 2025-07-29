class Solution:
    def solution_1412_5(self, word: str) -> int:
        n = len(word)
        
        # mark vowel
        # 'aba' vowels = [1, 0, 1]
        vowels = list(map(lambda x: int(x in 'aeiou'), word))
        
        # add vowel count in each substring
        # acc = [0, 1, 1, 2]
        acc = list(accumulate(vowels, initial=0))
        
        # add up vowel count
        # acc2 = [0, 1, 2, 4]
        acc2 = list(accumulate(acc))

        
        ans = 0
        for i in range(n+1):
            # add up accumulative vowel count in substring start from index i
            ans += acc2[-1] - acc2[i]
            # subtract previous vowel counts from current substrings
            if i > 0:
                ans -= (acc[i-1]) * (len(acc2) - i)
        
        return ans