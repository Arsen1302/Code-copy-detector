class Solution:
    def solution_1420_5(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        res = []
        cols = n // rows
        
        for i in range(cols):
            for j in range(i, n, cols+1):
                res.append(encodedText[j])  # it is observed that skipping cols+1 from a given pos gives the required char
                
        return ''.join(res).rstrip(' ')  # removes trailing spaces from right