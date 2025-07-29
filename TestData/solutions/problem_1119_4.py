class Solution(object):
    def solution_1119_4(self, word1, word2):
        count1 = dict()
        count2 = dict()
        
        for char in word1:
            count1[char] = count1.get(char, 0) + 1
        
        for char in word2:
            count2[char] = count2.get(char,0) + 1
        
        
        return sorted(count1.values()) == sorted(count2.values()) and set(word1)== set(word2)