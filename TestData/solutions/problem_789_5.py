class Solution:
    def solution_789_5(self, text):
        countText = Counter(text)
        countWord = Counter("balloon")
        return min(countText[c] // countWord[c] for c in countWord)