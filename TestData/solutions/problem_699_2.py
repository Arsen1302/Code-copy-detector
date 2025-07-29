class Solution:
    def solution_699_2(self, head: ListNode) -> List[int]:
        res, stack, idx = [], [], 0
        while head:
            while stack and stack[-1][0] < head.val:
                _, i = stack.pop()
                res[i] = head.val
            
            res.append(0)
            stack.append((head.val, idx))
            idx += 1
            head = head.next
        return res