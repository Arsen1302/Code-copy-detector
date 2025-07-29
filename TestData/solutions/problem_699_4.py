class Solution:
    def solution_699_4(self, head: ListNode) -> List[int]:
        lst = []
        stack = []
        res = []
        
        while head:
            lst.append(head.val)
            head = head.next
        
        for i in range(len(lst) - 1, -1, -1):
            max_prev = 0
            
            while stack and stack[-1] <= lst[i]:
                stack.pop()
            
            if stack:
                max_prev = stack[-1]
            
            res.append(max_prev)
            stack.append(lst[i])
        
        return reversed(res)