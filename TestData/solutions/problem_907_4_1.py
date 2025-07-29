class Solution:
    def solution_907_4_1(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def solution_907_4_2(root, head):
            
            if not head: 
                res[0] = True
                return 
        
            elif not root: return
            
            if root.val == head.val:
                solution_907_4_2(root.left, head.next)
                solution_907_4_2(root.right, head.next)
        
        
        def solution_907_4_3(root, head):
            if not root: return 
            
            if root.val == head.val:
                solution_907_4_2(root, head)
                
                
            solution_907_4_3(root.left, head)
            solution_907_4_3(root.right, head)
            
        res = [False]
        solution_907_4_3(root, head)
        return res[0]