class Solution:
    def solution_1119_5(self, word1: str, word2: str) -> bool:
        """
        operation 1 ~ swapping characters - this means that the order of the characters is not a problem since we can move them as we want
        operation 2 ~ same number of keys and same values at values - using 2 hashmaps of the 2 words you'll see that we only need the same keys and the same values 
        (not necessary allocated to the same key though since we can use operation 2 to move them around)
        """
        d1, d2 = {}, {}
        for i in range(len(word1)):
            if word1[i] not in d1:
                d1[word1[i]] = 1
            else:
                d1[word1[i]] += 1
        for i in range(len(word2)):
            if word2[i] not in d2:
                d2[word2[i]] = 1
            else:
                d2[word2[i]] += 1
        return sorted(d1.keys()) == sorted(d2.keys()) and sorted(d1.values()) == sorted(d2.values())