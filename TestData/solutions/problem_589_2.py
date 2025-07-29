class Solution:
    def solution_589_2(self, A: List[int]) -> List[int]:
        return sorted(A, key = lambda x : x % 2)

class Solution:
    def solution_589_2(self, A: List[int]) -> List[int]:
        return [i for i in A if not i % 2] + [i for i in A if i % 2]


- Junaid Mansuri
(LeetCode ID)@hotmail.com