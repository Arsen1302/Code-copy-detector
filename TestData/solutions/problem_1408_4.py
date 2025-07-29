class Solution:
    def solution_1408_4(self, head: Optional[ListNode]) -> List[int]:
        prev = head.val 
        node = head.next 
        dmin = inf 
        first = i = last = 0
        while node and node.next: 
            i += 1
            if prev < node.val > node.next.val or prev > node.val < node.next.val: 
                if last : dmin = min(dmin, i - last)
                last = i # last critical point 
                if not first: first = i # first critical point 
            prev = node.val 
            node = node.next 
        return [dmin, last - first] if dmin < inf else [-1, -1]