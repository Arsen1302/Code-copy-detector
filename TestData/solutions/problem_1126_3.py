class Solution:
    def solution_1126_3(self, sequence: str, word: str) -> int:
        c = 0
        for i in range(1,len(sequence)//len(word)+1):
            if word*i in sequence:
                c += 1
                continue
            break
        return c