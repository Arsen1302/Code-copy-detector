class Solution(object):
    def solution_54_1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
		if head is None or head.next is None return False
        slow_ref = head
        fast_ref = head
        while fast_ref and fast_ref.next:
            slow_ref = slow_ref.next
            fast_ref = fast_ref.next.next
            if slow_ref == fast_ref:
                return True
        return False
		
	If you get it please Upvote.