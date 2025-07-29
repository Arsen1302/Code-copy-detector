class Solution:
    def solution_1232_3(self, sentence1: str, sentence2: str) -> bool:
        
        if sentence1 == sentence2:
            return True

        # spplit the sentences into words
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")
        
        # kep the smaller one in words2
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        
        '''
        Keep following states during traversal
            0. not inserted
            1. inserting
            2. inserted
        '''
        inserted = 0
        i = 0
        j = 0

        while(i < len(words1)):
            if j >= len(words2):
                if inserted == 2:
                    return False
                else:
                    return True
            if words1[i] != words2[j]:
                if inserted == 0:
                    inserted = 1 # start insertion
                    i += 1 # only move i not j
                elif inserted == 1:
                    i += 1 # keep inserting more words
                else: # that means it's 2 .. hence a sentence is already inserted
                    return False # as not more sentences can be inserted
            else: # continue moving
                if inserted == 1:
                    inserted = 2 # set that previously a sentence has already been inserted
                i += 1
                j += 1
            
        # if we reach here then it means we can do it
        return j == len(words2)