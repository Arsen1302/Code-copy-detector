class Solution:
    def solution_282_5(self, a: int) -> List[int]:
    	for i in range(int(a**.5),-1,-1):
    		if a % i == 0: break
    	return [a//i,i]
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com