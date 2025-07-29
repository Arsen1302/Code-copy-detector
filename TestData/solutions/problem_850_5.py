class Solution:
    def solution_850_5(self, s: str, M: int, m: int, _: int) -> int:
        L, D = len(s), collections.defaultdict(int)
        for j in range(L+1-m): D[s[j:j+m]] += (len(set(s[j:j+m])) <= M)
        return max(D.values())
		
		
- Junaid Mansuri
- Chicago, IL