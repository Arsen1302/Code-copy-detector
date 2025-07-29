class Solution:
    def solution_1320_5(self, text: str, brokenLetters: str) -> int:
        return len([i for i in text.split(' ') if len(set(i).intersection(brokenLetters))==0])