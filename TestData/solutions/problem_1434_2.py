class Solution:
	def solution_1434_2(self, head: Optional[ListNode]) -> Optional[ListNode]:

		if head.next == None:
			return

		slow, fast = head, head
		prev = None

		while fast and fast.next:
			prev = slow
			slow = slow.next
			fast = fast.next.next

		prev.next = slow.next

		return head