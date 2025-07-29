class Solution:
    def solution_693_2(self, A: List[int]) -> bool:
    	return (lambda x,y: x in y and 2*x in y and 3*x in y)(sum(A)//3,itertools.accumulate(A))
				
				
				
Junaid Mansuri
Chicago, IL