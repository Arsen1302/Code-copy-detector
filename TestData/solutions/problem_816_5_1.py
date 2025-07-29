class Solution:
    def solution_816_5_1(self, words, index, word):
        if len(word) != len(set(word)):
            return
        self.ans = max(self.ans, len(word))
        if index == len(words):
            return
        for i in range(index, len(words)):
            self.solution_816_5_1(words, i+1, word+words[i])
    
    def solution_816_5_2(self, arr: List[str]) -> int:
        self.ans = 0
        self.solution_816_5_1(arr, 0, '')
        return self.ans