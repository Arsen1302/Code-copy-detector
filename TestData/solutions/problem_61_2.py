class Solution:
	def solution_61_2(self, head: Optional[ListNode]) -> Optional[ListNode]:

		new_node=head

		result = new_node

		array = []

		while head != None:
			array.append(head.val)
			head=head.next

		array = sorted(array)

		for num in array:
			new_node.val = num
			new_node = new_node.next

		return result