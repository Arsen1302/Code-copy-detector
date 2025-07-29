class Solution:
    def solution_289_2(self, words):
        letters_a, letters_b, letters_c = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        row_words = []
        for word in words:
            unique_word = set(word.lower())
            if unique_word <= letters_a or unique_word <= letters_b or unique_word <= letters_c:
                row_words.append(word)
        return row_words