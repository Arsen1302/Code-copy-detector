class Solution:
    def solution_1703_4_1(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        def solution_1703_4_2(word1, word2):
            count = 0
            
            for a, b in zip(word1, word2):
                if a != b:
                    count += 1
            
            return count
        
        res = []
        for word in queries:
            for item in dictionary:
                x = solution_1703_4_2(word, item)
                if x <= 2:
                    res.append(word)
                    break
        return res