class Solution:
    def solution_1166_4(self, head: ListNode, k: int) -> ListNode:
        vals = []
        node = head
        while node: 
            vals.append(node.val)
            node = node.next 
            
        vals[k-1], vals[-k] = vals[-k], vals[k-1]
        dummy = node = ListNode()
        for x in vals:
            node.next = node = ListNode(x)
        return dummy.next