class Solution:
    def solution_1408_5_1(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return [-1, -1]
        
        prev, curr = head, head.next
        idx = 1
        res = []
        while curr and curr.next:
            if self.solution_1408_5_2(prev.val, curr.val, curr.next.val):
                res.append(idx)
            
            prev = curr
            curr = curr.next
            idx += 1
        
        if len(res) <= 1: return [-1, -1]
        min_ = min(res[i] - res[i-1] for i in range(1, len(res)))
        max_ = res[-1] - res[0]
        return [min_, max_]
    
    def solution_1408_5_2(self, prev, curr, nxt):
        return (prev > curr < nxt) or (prev < curr > nxt)