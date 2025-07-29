class Solution:
    def solution_505_3(self, H: ListNode, G: List[int]) -> int:
        S, c = set(G), 0
        while H != None: c, H = c + (H.val in S and (H.next == None or H.next.val not in S)), H.next
        return c
		

- Junaid Mansuri
- Chicago, IL