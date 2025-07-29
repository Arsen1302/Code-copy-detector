class Solution:
    def solution_780_5_1(self, queries: List[str], words: List[str]) -> List[int]:
        queries_frequecy = [self.solution_780_5_2(i) for i in queries]
        words_frequecy = [self.solution_780_5_2(i) for i in words]
        words_frequecy.sort()
        res = []
        length = len(words_frequecy)
        for i in range(len(queries_frequecy)):
            for j in range(length):
                if queries_frequecy[i] < words_frequecy[j]:
                    res.append(length -j)
                    break
            if len(res) < i+1:
                res.append(0)
        return res
                    
    def solution_780_5_2(self, s):
        smallest = min(s)
        return s.count(smallest)