class Solution:
    def solution_537_3(self, seats: List[int]) -> int:
    	L = len(seats)
    	S = [i for i in range(L) if seats[i]]
    	d = [S[i+1]-S[i] for i in range(len(S)-1)] if len(S) > 1 else [0]
    	return max(max(d)//2, S[0], L-1-S[-1])
		
		
- Python 3
- Junaid Mansuri