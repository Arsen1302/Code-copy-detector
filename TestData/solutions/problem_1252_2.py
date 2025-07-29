class Solution:
    def solution_1252_2(self, word: str) -> int:
        ans = 0
        cnt = unique = 1
        for i in range(1, len(word)): 
            if word[i-1] <= word[i]: 
                cnt += 1
                if word[i-1] < word[i]: unique += 1
            else: cnt = unique = 1
            if unique == 5: ans = max(ans, cnt)
        return ans