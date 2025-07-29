class Solution:
    def solution_428_2(self, words: List[str]) -> str:
        words.sort()
        max_len = 1
        symbol = ']'
        ans = None
        for i in range(len(words)):
            if len(words[i]) == 1:
                words[i] = words[i] + symbol
                if max_len < len(words[i]):
                    max_len = len(words[i])
                    ans = words[i]
            else:
                word = words[i][:-1] + symbol
                index = bisect.bisect_left(words, word)
                if index < len(words) and words[index] == word:
                    words[i] = words[i] + symbol
                    if max_len < len(words[i]):
                        max_len = len(words[i])
                        ans = words[i]
        if not ans:
            return ""
        return ans[:-1]