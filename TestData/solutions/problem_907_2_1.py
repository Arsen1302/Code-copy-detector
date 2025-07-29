class Solution:
    def solution_907_2_1(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def solution_907_2_2(hd,node):
            if not hd.next :
                return hd.val==node.val
            if hd.val==node.val:
                if node.left and node.right:
                    return solution_907_2_2(hd.next,node.left) or solution_907_2_2(hd.next,node.right)
                elif node.left:
                    return solution_907_2_2(hd.next,node.left) 
                elif node.right :
                    return solution_907_2_2(hd.next,node.right)
                else:
                    return False
            else:
                return False
        stk=[root]
        while stk:
            temp=stk.pop()
            if solution_907_2_2(head,temp):
                return True
            if temp.left:
                stk.append(temp.left)
            if temp.right:
                stk.append(temp.right)
        return False