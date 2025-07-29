class Solution:
    def solution_119_5_1(self, head, node):
        if not node:
            return (head, True)
        
        cur, is_palindrome = self.solution_119_5_1(head, node.next)
        if not is_palindrome:
            return (None, False)
        if cur.val != node.val:
            return (None, False)
        return (cur.next, True)
        
    def solution_119_5_2(self, head: ListNode) -> bool:
        return self.solution_119_5_1(head, head)[1]