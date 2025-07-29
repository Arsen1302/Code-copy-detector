class Solution:
	def solution_162_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if head is None or head.next is None:
			return head

		e,o = head,head.next
		odd_head = o
		while o!=None and o.next!=None:
			e.next = o.next
			e = e.next
			o.next = e.next
			o = o.next

		e.next = odd_head
		return head