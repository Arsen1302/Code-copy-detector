class Solution:
    def solution_1628_4(self, grades: List[int]) -> int:
        n=len(grades)
        k=0
        while n>=k+1:
            k+=1
            n-=k
        return k