class Solution:
    def solution_1420_3(self, s: str, rows: int) -> str:
        if not s: return ""
        n=len(s)
        cols=n//rows
        arr=[" "]*n
        for i in range(rows):
            for j in range(cols):
                if i>j: continue
                arr[i+rows*(j-i)]=s[i*cols+j]
        i=n-1
        while i>=0 and arr[i]==" ":
            i-=1
        return ''.join(arr[:i+1])