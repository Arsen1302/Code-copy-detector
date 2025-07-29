class Solution:
    def solution_623_2(self, S: str) -> List[int]:
    	return (lambda x: [x.pop() if i == 'D' else x.popleft() for i in S]+[x[0]])(collections.deque(range(len(S)+1)))
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com