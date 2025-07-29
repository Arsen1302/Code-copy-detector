class Solution:
    def solution_893_1(self, S: str, T: str) -> int:
        D = collections.Counter(S) - collections.Counter(T)
        return sum(max(0, D[s]) for s in set(S))
		
		
- Junaid Mansuri
- Chicago, IL