class Solution:
    def solution_1510_3(self, s: str) -> List[str]:
        row1 = int(s[1])
        row2 = int(s[4])
        col1 = ord(s[0]) # To get their Unicode values
        col2 = ord(s[3]) # To get their Unicode values
        res = []
        # Since we are asked to sort the answer list first column and then row wise.
        for i in range(col1, col2+1):  
            for j in range(row1, row2+1):
                res.append(f"{chr(i)}{j}") # First column then row
        return res