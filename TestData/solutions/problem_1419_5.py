class Solution:
    def solution_1419_5(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        l = []
        temp = head
        i = 1
        while temp:
            z = []
            for j in range(i):
                if temp:
                    z.append(temp.val)
                    temp = temp.next
            if len(z) % 2 == 0:
                z = z[::-1]
            l.append((z))
            i += 1
        head = ListNode(l[0][0])
        temp = head
        i = 1
        while i < len(l):
            for j in range(len(l[i])):
                p = ListNode(l[i][j])
                temp.next = p
                temp = temp.next
            i += 1
        return head