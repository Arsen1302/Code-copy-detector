class Solution:
    def solution_1415_4(self, word1: str, word2: str) -> bool:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for i in word1:
            dic1[i] += 1
        for j in word2:
            dic2[j] += 1
        
        for k,v in dic1.items():
            if abs(v-dic2[k]) > 3:
                return False
        for k,v in dic2.items():
            if abs(v-dic1[k]) > 3:
                return False
        else:
            return True