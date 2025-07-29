class Solution:
    def solution_245_4(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2, curr1, curr2, head, carry = [], [], l1, l2, ListNode(), 0
        while curr1 is not None:
            stack1.append(curr1.val)
            curr1 = curr1.next
        while curr2 is not None:
            stack2.append(curr2.val)
            curr2 = curr2.next
        l1, l2 = len(stack1), len(stack2)
        for _ in range(max(l1, l2)):
            a = 0 if l1 <= 0 else stack1.pop()
            b = 0 if l2 <= 0 else stack2.pop()
            l1 -= 1
            l2 -= 1
            sum = a+b+carry
            carry = sum//10
            temp = ListNode(sum%10, head.next)
            head.next = temp
        if carry != 0:
            temp = ListNode(carry, head.next)
            head.next = temp
        return head.next