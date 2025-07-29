class Solution:
    def solution_428_3(self, words: List[str]) -> str:
        word_map = {}
        max_len = 0
        for word in sorted(words):
            if len(word) == 1:
                word_map[word] = True
                max_len = max(max_len, len(word))
            elif word_map.get(word[:-1]):
                word_map[word] = True
                max_len = max(max_len, len(word))
            else:
                word_map[word] = False
        
        answers = [word for word, flag in word_map.items() if flag and len(word) == max_len]
        if len(answers) > 0:
            return min(answers)
        return ""