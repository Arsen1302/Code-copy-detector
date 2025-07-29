class Solution:
    def solution_1419_2_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start_joint = head 
        group_size = 1
        while start_joint and start_joint.next: 
            group_size += 1
            start = end = start_joint.next 
            group_num = 1 
            while end and end.next and group_num < group_size: 
                end = end.next 
                group_num += 1 
            end_joint = end.next 
            if group_num % 2 != 0: 
                start_joint = end 
                continue 
            start_joint.next = self.solution_1419_2_2(start, end, end_joint)
            start_joint = start 
        return head
    def solution_1419_2_2(self, start, end, end_joint): 
        prev, curr = end_joint, start
        while curr and curr != end_joint: 
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        return prev