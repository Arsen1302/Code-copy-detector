class Solution:
    def solution_428_4_1(self, words: List[str]) -> str:
        # solution_428_4_2 + memo
        # Complexity Analysis:
            # Time: O(NK)
            # Space: O(N)
        
        max_word = ''
        
        def solution_428_4_2(word):
            nonlocal max_word            
            if word in memo: return memo[word]                        
            
            curr_len = 0
            
            if word == '':
                curr_len = 0                
            elif word[:-1] in words_set:
                curr_len = 1 + solution_428_4_2(word[:-1])                                
            else:
                curr_len = float('-inf')                
            
            if curr_len > len(max_word) or (curr_len == len(max_word) and word < max_word):                
                max_word = word
                        
            memo[word] = curr_len
            return curr_len
            
        
        # create words set                                
        words_set = set(words)
        words_set.add('')
        memo = {}
        
        # iterate words
        for word in words:
            # call solution_428_4_2 for each word
            solution_428_4_2(word)
            
        return max_word