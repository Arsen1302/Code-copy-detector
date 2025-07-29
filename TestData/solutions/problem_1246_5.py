class Solution:
    def solution_1246_5(self, sentence: str) -> bool:
        return(len(set(list(sentence))) == 26)