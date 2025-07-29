class Solution:
    def solution_1320_1(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        length = len(text)
        brokenLetters = set(brokenLetters)

        for word in text:
            for char in word:
                if char in brokenLetters:
                    length -= 1
                    break
					
        return length