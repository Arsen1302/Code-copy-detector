class Solution:
    def solution_775_5_1(self, words, chars):
        d, total = Counter(chars), 0
        for w in words: total += self.solution_775_5_2(w, d.copy())
        return total
    
    def solution_775_5_2(self, w, d):
        for c in w:
            if c not in d or d[c] == 0: return 0
            else: d[c]-=1
        return len(w)