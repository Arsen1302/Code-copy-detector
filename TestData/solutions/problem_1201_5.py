class Solution:
    def solution_1201_5(self, word1: str, word2: str) -> str:
        minimum = min(len(word1),len(word2))
        finalword=""
        count=0
        #first combine words until they have same length
        for i in range(minimum):
            finalword = finalword +word1[i]+word2[i]
            count= count+1
        #if word1 or word2 has unequal length 
        if len(word1)>len(word2):
            finalword = finalword + word1[count:]
        elif len(word2) > len(word1):
            finalword = finalword + word2[count:]
        return(finalword)