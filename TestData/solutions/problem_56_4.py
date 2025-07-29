class Solution:
    def solution_56_4(self, H: ListNode) -> None:
        if H == None: return None
        C, A = H, []
        while C != None: A.append(C); C = C.next
        M = len(A)//2
        for i in range(M): A[i].next, A[-(i+1)].next = A[-(i+1)], A[i+1]
        A[M].next = None
        return H
		
		
- Junaid Mansuri
- Chicago, IL