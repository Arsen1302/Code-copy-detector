class Solution:
	def solution_69_4_1(self, head: ListNode):
		while ( head ):
			head.val *= -1
			head = head.next
	
	def solution_69_4_2(self, headA: ListNode, headB: ListNode) -> ListNode:
		self.solution_69_4_1(headA)
		
		while ( headB ):
			if headB.val < 0:break
			headB = headB.next
		
		self.solution_69_4_1(headA)
		return headB