class Solution:
    def solution_726_3_1(self, words: List[str]) -> int:
        w_set = set(words)
        @cache
        def solution_726_3_2(w:str) -> int:
            return 1 + max((solution_726_3_2(s) for i in range(len(w)) if (s:=w[:i]+w[i+1:]) in w_set), default=0)
        return max(solution_726_3_2(w) for w in words)