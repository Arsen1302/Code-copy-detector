class Solution:
    def solution_1166_3(self, head: ListNode, k: int) -> ListNode:
        res = []
        curr =  head
        
        while curr is not None:
            res.append(curr)
            curr = curr.next
        res[k-1].val, res[len(res)-k].val = res[len(res)-k].val, res[k-1].val
        return head