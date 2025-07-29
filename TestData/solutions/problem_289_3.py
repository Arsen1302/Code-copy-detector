class Solution:
    def solution_289_3(self, words):
        keyboard = r'(?i)^(?:[qwertyuiop]+|[asdfghjkl]+|[zxcvbnm]+)$'
        row_words = []
        for word in words:
            if word == "":
                row_words.append("")
            row_words.extend(re.findall(keyboard, word))

        return row_words