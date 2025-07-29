class Solution:
    def solution_885_4(self, A: List[int]) -> int:
        for i,v in enumerate(itertools.accumulate(sorted(collections.Counter(A).values(), reverse = True))):
            if v >= len(A)//2: return i + 1

			
- Junaid Mansuri
- Chicago, IL