class Solution:
    def solution_1027_5(self, s: str) -> int:
        """
        index    0   1   2    3 
        value    a.  b.  a    c
        prefix   a   ab  aba  abac
        sufix.   c   ca. cab  caba
        prelen   1   2    2
        suflen.  1   2    3
        
        
        """
        prefixSet = set()
        sufixSet = set()
        prelen =[]
        suflen = []
        
        n = len(s)
        
        for i in range(n):
            prefixSet.add(s[i])
            sufixSet.add(s[n - i - 1])
            prelen.append(len(prefixSet))
            suflen.append(len(sufixSet))
        print(prelen,suflen )
        
        count = 0
        for i in range(n - 1):
            if prelen[i] == suflen[n-i-2]:
                count += 1
        return count