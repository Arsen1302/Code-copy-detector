class Solution:
    def solution_1258_3_1(self, s: str) -> bool:
        self.res = False
        def solution_1258_3_2(s, k):
            n1 = int(s[:k+1])
            for j in range(k+1, len(s)):
                n2 = int(s[k+1:j+1])
                if n1 - n2 == 1:
                    if j == len(s)-1:
                        self.res = True 
                    else: 
                        solution_1258_3_2(s[k+1:], j-(k+1))
                if n2 >= n1:
                    break
                        
        for i in range(len(s)):
            solution_1258_3_2(s, i)
        return self.res