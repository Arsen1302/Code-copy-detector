class Solution:
    def solution_409_2(self, words, k):
        dicktionary = defaultdict(int)
        for i in words: dicktionary[i] += 1
        
        sorted_dick = sorted(dicktionary.items(), key=lambda x: (-x[1], x[0]))
        
        return [i[0] for i in sorted_dick][:k]