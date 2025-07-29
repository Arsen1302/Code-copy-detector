class Solution(object):
    def solution_289_5(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_list=[]
        top_row=set('qwertyuiop')
        mid_row=set('asdfghjkl')
        bottom_row=set('zxcvbnm')
        for word in words:
            if set(word.lower()).issubset(top_row) or set(word.lower()).issubset(mid_row) or set(word.lower()).issubset(bottom_row):
                word_list.append(word)
        return word_list