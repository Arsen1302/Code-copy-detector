class Solution:
    def solution_22_5_1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        nums = []
        L = 0
        while head is not None:
            nums.append(head.val)
            head = head.next
            L += 1
        #Convert to array first
        root = TreeNode(val=0)
        def solution_22_5_2(node, nums, lo, hi):
            if lo > hi:
                return None
			#Algorithm: Due to the balanced requirement, the inserted value has to be in the middle. 
			#This process is similar to binary search, or quick sort. In fact, quick sort is to build a binary search tree. 
			#That's why if the array is sorted already and pivot was not randomly selected, the time complexity goes up to O(n^2),
			#because the binary search tree became "IMBALANCED" and become a one-sided tree (or a linked list)
            mid = (lo+hi)//2
            node = TreeNode(val=nums[mid])
            node.left = solution_22_5_2(node.left, nums, lo, mid-1)
            node.right = solution_22_5_2(node.right, nums, mid+1, hi)
            return node
        
        root = solution_22_5_2(root, nums, 0, L-1)
        return root