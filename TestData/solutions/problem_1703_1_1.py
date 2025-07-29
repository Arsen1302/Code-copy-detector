class Solution:
    def solution_1703_1_1(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # T: ((N + M) * L^3), S: O(M * L^3)
        N, M, L = len(queries), len(dictionary), len(queries[0])
        validWords = set()
        
        for word in dictionary:
            for w in self.solution_1703_1_2(word):
                validWords.add(w)
        
        ans = []
        for word in queries:
            for w in self.solution_1703_1_2(word):
                if w in validWords:
                    ans.append(word)
                    break

        return ans
    
    def solution_1703_1_2(self, word):
        # T: O(L^3)
        L = len(word)
        for i in range(L):
            yield word[:i] + "*" + word[i+1:]

        for i, j in itertools.combinations(range(L), 2):
            yield word[:i] + "*" + word[i+1:j] + "*" + word[j+1:]