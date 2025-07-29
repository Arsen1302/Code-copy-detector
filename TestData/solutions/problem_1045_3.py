class Solution:
    def solution_1045_3(self, a):
        return any(True for i,x in enumerate(a) if i<len(a)-2 and a[i]%2==a[i+1]%2==a[i+2]%2==1)