class Solution:
    def solution_688_3(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])  # start with the root node of the BST
        for i in range(1, len(preorder)):  # for each successive element:
            curr = root  # 1. start at the root node
            while True:  # 2. traverse to the appropriate parent node
                if preorder[i] < curr.val:
                    if not curr.left:  # appropriate parent node reached
                        curr.left = TreeNode(preorder[i])
                        break  # node added, go to the next element
                    curr = curr.left
                else:
                    if not curr.right:  # appropriate parent node reached
                        curr.right = TreeNode(preorder[i])
                        break  # node added, go to the next element
                    curr = curr.right
        return root