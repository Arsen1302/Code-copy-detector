class Solution:
    def solution_844_5(self, head: ListNode) -> int:
        binaryNumberString = ""
        while head:
            binaryNumberString += str(head.val)
            head = head.next
        return int(binaryNumberString,2)