class Solution:
    def solution_497_1_1(self, s: str, words: List[str]) -> int:
        
        def solution_497_1_2(word):
            res = []
            
            n = len(word)
            i, j = 0, 0
            while i<=j and j <= n-1:
                while j <= n-1 and word[j] == word[i]:
                    j += 1
                res.append(word[i])
                res.append(j-i)
                i = j
            return res
        
        t = 0 
        start = solution_497_1_2(s)
        n = len(start)//2
        def solution_497_1_3(w):
            r = solution_497_1_2(w)
        
            if len(r) != len(start):
                return False 
            for i in range(0, 2*n, 2):
                if start[i] != r[i]:
                    return False
                elif start[i] == r[i]:
                    if start[i+1] < r[i+1]:
                        return False
                    elif start[i+1] == r[i+1]:
                        pass 
                    elif start[i+1] < 3:
                        return False
            return True

        for w in words:
            if solution_497_1_3(w):
                t += 1
        return t