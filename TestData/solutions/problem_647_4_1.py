class Solution:

    # a static vowel set so we don't initialize it with every quer
    vowel_set = set(('a', 'e', 'i', 'o', 'u'))
    
    def solution_647_4_1(self, wordlist: List[str], queries: List[str]) -> List[str]:

        # keep a set of all variations in their original form for fast lookup
        wordset = set(wordlist)

        # put all the words into the wordlist (lowercase) and lowercase without vowels
        # we will use these dicts to check for the capitalization errors and vowel errors
        # which are both cas insensitive (so lower both)
        #
        # also we only keep the first occurencce to match the precedence rules
        worddict = dict()
        wrddct = dict()
        for idx, word in enumerate(wordlist):
            lowered = word.lower()
            devoweled = self.solution_647_4_2(lowered)
            if lowered not in worddict:
                worddict[lowered] = word
            if devoweled not in wrddct:
                wrddct[devoweled] = word
        
        # go through each of the queries and check the rules
        result = []
        for query in queries:

            # check if it is in the original wordlist
            # append the word and continue with the next query
            if query in wordset:
                result.append(query)
                continue
            
            # check if the word only has capitalization error
            # append the corrected one and continue with the next query
            lowered = query.lower()
            if lowered in worddict:
                result.append(worddict[lowered])
                continue
            
            # check if the word has vowel errors, append it to the result
            # and go to the next query
            devoweled = self.solution_647_4_2(lowered)
            if devoweled in wrddct:
                result.append(wrddct[devoweled])
                continue
            
            # no case matched (all quard clauses have been passed)
            result.append("")
            
        return result
    
    def solution_647_4_2(self, word):
        # replace vowels with unused placeholder
        return "".join(char if char not in self.vowel_set else "_" for char in word)