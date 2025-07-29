class Solution:
    def solution_497_4_1(self, s: str, words: List[str]) -> int:
        # edge cases
        if len(s) == 0 and len(words) != 0:
            return False
        if len(words) == 0 and len(s) != 0:
            return False
        if len(s) == 0 and len(words) == 0:
            return True
     
        # helper function, compressing string and extract counts
        def solution_497_4_2(s_word):
            init_string =[s_word[0]]
            array = []
            start = 0
            for i,c in enumerate(s_word):
                if c == init_string[-1]:
                    continue
                array.append(i-start)
                start = i
                init_string += c  
            array.append(i-start+1)    
            return init_string,array

        res = len(words)
        s_split, s_array = solution_497_4_2(s)
        for word in words:
            word_split = ['']
            word_array = []
            word_split,word_array = solution_497_4_2(word)
            if s_split == word_split:
                for num_s,num_word in zip(s_array,word_array):
                    if num_s != num_word and num_s < 3 or num_word > num_s:
                        res -= 1
                        break
            else:
                res -= 1
        return res