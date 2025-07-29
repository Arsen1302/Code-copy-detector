class Solution:
    def solution_940_5(self, words):
        words.sort(key=len)

        res = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
        return set(res)