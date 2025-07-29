class Solution:
    def solution_1461_3_1(self, head: Optional[ListNode]) -> int:

        mid = self.solution_1461_3_2(head)
        rev = self.solution_1461_3_4(mid)
        max = self.solution_1461_3_3(head, rev, -inf)

        return max
    def solution_1461_3_2(self, list):
        slow, fast = list, list
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
    
    def solution_1461_3_3(self, a, b, cur_max):
        if b is None:
            return cur_max

        sum = a.val + b.val
        if sum > cur_max:
            cur_max = sum

        return self.solution_1461_3_3(a.next, b.next, cur_max)

    def solution_1461_3_4(self, head):
        cur, prev = head, None

        while cur:       
            cur.next, prev, cur = prev, cur, cur.next

        return prev
	```