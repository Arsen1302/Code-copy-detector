class Solution:
    def solution_1126_4(self, sequence: str, word: str) -> int:
        n=len(sequence)
        m=len(word)
        c=0
        for i in range(1,(n//m)+1):
            s=word*i
            if sequence.find(s)!=-1:
                c=i
        return c