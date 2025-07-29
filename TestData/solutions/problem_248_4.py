class Solution:
    def solution_248_4(self, n: List[int]) -> List[int]:
    	N = set(n)
    	return [i for i in range(1, len(n) + 1) if i not in N]

- Python 3
(LeetCode ID)@hotmail.com