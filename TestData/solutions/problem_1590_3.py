class Solution:
    def solution_1590_3(self, brackets: List[List[int]], income: int) -> float:
        lower = 0; 
		tax = 0; 
		left = income # amount left to be taxed
        for i in brackets:
            k = i[0]-lower # amount being taxed
            if k<= left:
                tax+=k*i[1]/100;  left-=k;  lower=i[0]
            else:
                tax+= left*i[1]/100
                break
        return tax