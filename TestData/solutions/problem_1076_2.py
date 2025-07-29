class Solution(object):
    def solution_1076_2(self, text):
        word_list = text.split()
        words, spaces = len(word_list), text.count(" ")
        
        if words > 1:
            q, r = spaces//(words-1), spaces%(words-1)
        else:
            q, r = 0, spaces
        
        return (" " * q).join(word_list) + " " * r