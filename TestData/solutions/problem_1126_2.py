class Solution:
    def solution_1126_2(self, sequence: str, word: str) -> int:
        for i in range(len(sequence)//len(word)+1,0,-1):
            if i*word in sequence:
                return i
        else:
            return 0