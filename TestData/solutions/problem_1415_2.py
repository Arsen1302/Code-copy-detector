class Solution:
    def solution_1415_2(self, word1: str, word2: str) -> bool:
        
        # make an array to track occurences for every letter of the
        # alphabet
        alphabet = [0]*26
        
        # go through both words and count occurences
        # word 1 add and word 2 subtract
        # after this we have the differences for every letter
        for index in range(len(word1)):
            alphabet[ord(word1[index]) - 97] += 1
            alphabet[ord(word2[index]) - 97] -= 1
        
        # find min and max and check that it is less than three
        return min(alphabet) >= -3 and max(alphabet) <= 3