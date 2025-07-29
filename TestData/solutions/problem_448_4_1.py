class Solution:
    def solution_448_4_1(self, licensePlate: str, words: List[str]) -> str:
        license = defaultdict(int)
        for s in licensePlate:
            if s.isalpha():
                license[s.lower()] += 1
                
        cand = ""
        candlen = float('inf')
        
        def solution_448_4_2(word):
            count = defaultdict(int)
            for w in word:
                count[w] += 1
            for w in license:
                if count[w] < license[w]:
                    return False
            return True
        
        for word in words:
            if solution_448_4_2(word):
                if len(word) < candlen:
                    cand = word
                    candlen = len(word)
        
        return cand