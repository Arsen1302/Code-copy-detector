class Solution:
    def solution_169_3_1(self, words):
        @cache
        def solution_169_3_2(string):
            l, r = 0, len(string)-1
            while l < r:
                if string[l] != string[r]:
                    return False
                l+=1
                r-=1
            return True
                
        output = set()
        words_idx = {w:idx for idx,w in enumerate(words)}

        # Index of empty string
        idx_empty = -1
        if "" in words_idx:
            idx_empty = words_idx[""]

        for idx, word in enumerate(words):
            # To handle cases with empty string
            if solution_169_3_2(word) and word != "" and idx_empty != -1:
                    output.add((idx_empty, idx))
                    output.add((idx, idx_empty))

            substring = ""
            for i in range(len(word)):
                substring += word[i]
                # Where suffix is solution_169_3_2
                if substring[::-1] in words_idx and solution_169_3_2(word[i+1:]) and idx != words_idx[substring[::-1]]:
                    output.add((idx, words_idx[substring[::-1]]))

                # Where prefix is solution_169_3_2 
                if word[i+1:][::-1] in words_idx and solution_169_3_2(substring) and idx != words_idx[word[i+1:][::-1]]:
                    output.add((words_idx[word[i+1:][::-1]], idx))
            
        return output