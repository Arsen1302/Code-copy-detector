class Solution:
    def solution_22_4_1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def solution_22_4_2(nums):
            if not nums:
                return None
            
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            node.left = solution_22_4_2(nums[:mid])
            node.right = solution_22_4_2(nums[mid+1:])
            return node
        
        return solution_22_4_2(nums)