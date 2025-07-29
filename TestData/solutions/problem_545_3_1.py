class Solution:
    def solution_545_3_1(self, p: int, q: int) -> int:
       
	   def solution_545_3_2(right, up, distance):
            if distance == p:
                return 1 if (up and right) else 2 if up else 0
            elif distance > p:
                return solution_545_3_2(not right, not up, distance % p)
            else:
                return solution_545_3_2(not right, up, distance+q)
        
        return solution_545_3_2(True, True, q)