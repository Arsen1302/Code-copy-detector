class Solution:
    def solution_69_5(self, A: ListNode, B: ListNode) -> ListNode:
        S = set()
        while A != None: A, _ = A.next, S.add(A) 
        while B != None:
            if B in S: return B
            B = B.next
		
		
- Junaid Mansuri
- Chicago, IL