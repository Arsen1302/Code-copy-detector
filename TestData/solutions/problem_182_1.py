class Solution:
    def solution_182_1(self, x: int, y: int, z: int) -> bool:
        return False if x + y < z else True if x + y == 0 else not z % math.gcd(x,y)
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com