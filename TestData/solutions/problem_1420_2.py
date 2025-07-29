class Solution:
    def solution_1420_2(self, encodedText: str, rows: int) -> str:
        #print(len(encodedText),rows,len(encodedText)//rows)
        if len(encodedText)==0:
            return ""
        ans =''
        x =[]
        c = len(encodedText)//rows
        for i in range(0,len(encodedText),c):
            x.append(list(encodedText[i:i+c]))
        #print(x)
        for i in range(c):
            k = i
            p=''
            for j in range(rows):
                try:
                    p = p+x[j][k]
                except:
                    pass
                k = k+1
            ans = ans+p
        return ans.rstrip()