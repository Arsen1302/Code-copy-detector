class Solution:
    def solution_524_1(self, rec1: List[int], rec2: List[int]) -> bool:
        [A,B,C,D], [E,F,G,H] = rec1, rec2
        return F<D and E<C and B<H and A<G
		
		
- Python 3
- Junaid Mansuri