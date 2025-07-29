class Solution:
    def solution_763_3(self, arr1: List[int], arr2: List[int]) -> int:
        A=[]
        B=[]
        C=[]
        D=[]
        n=len(arr1)
        for i in range(n):
            A.append(arr1[i]+arr2[i]+i)
            B.append(arr1[i]+arr2[i]-i)
            C.append(arr1[i]-arr2[i]+i)
            D.append(arr1[i]-arr2[i]-i)
        a=max(A)-min(A)
        b=max(B)-min(B)
        c=max(C)-min(C)
        d=max(D)-min(D)
        return max(a,b,c,d)