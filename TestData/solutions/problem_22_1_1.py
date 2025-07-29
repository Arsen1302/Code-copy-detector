class Solution:
    l = 'left'
    r = 'right'
    
    def solution_22_1_1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        mid = len(nums) // 2
        treeNode = TreeNode(nums[mid])
        
        self.solution_22_1_2(nums[:mid], self.l, treeNode)
        self.solution_22_1_2(nums[(mid + 1):], self.r, treeNode)
        
        return treeNode
            
            
    def solution_22_1_2(self, nums, direction, treeNode):
        if len(nums) <= 0: return
        
        mid = len(nums) // 2
        left, right = nums[:mid], nums[(mid + 1):]
        
        if direction == self.l:
            treeNode.left = TreeNode(nums[mid])
            self.solution_22_1_2(left, self.l, treeNode.left)
            self.solution_22_1_2(right, self.r, treeNode.left)
        else:
            treeNode.right = TreeNode(nums[mid])
            self.solution_22_1_2(left, self.l, treeNode.right)
            self.solution_22_1_2(right, self.r, treeNode.right)