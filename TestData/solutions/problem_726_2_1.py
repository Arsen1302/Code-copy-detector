class Solution:
    def solution_726_2_1(self, words: List[str]) -> int:
        n=len(words)
        words_set={w:idx for idx, w in enumerate(words)}
        
        @cache
        def solution_726_2_2(i):                 
            curr=words[i]
            max_length=0
            for idx in range(len(curr)):
                new_wc = curr[:idx] + curr[idx+1:]
                if new_wc in words_set:
                    max_length=max(max_length, 1 + solution_726_2_2(words_set[new_wc]))
        
            return max_length
        
        return max(solution_726_2_2(i)+1 for i in range(n))