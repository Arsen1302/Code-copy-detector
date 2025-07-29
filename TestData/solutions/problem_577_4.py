class Solution:
    def solution_577_4(self, words: List[str], pattern: str) -> List[str]:
        patternIndex = "" #To store the index of the pattern
        for i in pattern: #Traverse the pattern string and add the index.
            patternIndex += str(pattern.index(i))
        #print(patternIndex)
        wordLisIndex = [] #To store the index of the pattern of each word in the list
        for i in words: #Traverse the words list
            patIndex = "" #To store the index of the i
            for j in i: #Traverse the i string and add the index.
                patIndex += str(i.index(j))
            wordLisIndex.append(patIndex)#Append the pat
        #print(wordLisIndex)
        patternMatch = [] #To store the matched pattern
        for pat in range(len(wordLisIndex)): #Traverse the wordLisIndex
            if patternIndex == wordLisIndex[pat]:#If their is a match append in patternMatch
                patternMatch.append(words[pat])
        return patternMatch