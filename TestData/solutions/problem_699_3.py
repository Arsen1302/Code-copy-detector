class Solution:
    def solution_699_3(self, head: ListNode) -> List[int]:
        res = []
        stack = []
        
        idx = 0
        while head:
            res.append(0)
            
            while stack and stack[-1][0] < head.val:
                _, index = stack.pop()
                res[index] = head.val
            
            stack.append((head.val, idx))
            idx += 1
            
            head = head.next
        
        return res