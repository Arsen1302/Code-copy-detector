class Solution:
    def solution_1435_5_1(self, node, src_val, dest_val):
        # To handle pre-order iterative
        stack = []
        stack.append((node, ""))
        # Tracking the path to both start and destination
        src_path = dest_path = ""
        
        while stack:
            node, path = stack.pop()
            
            if node.val == src_val:
                src_path = path
            if node.val == dest_val:
                dest_path = path
            
            # Tracking the both paths at the same time
            if node.right:
                stack.append((node.right, path+"R"))
            if node.left:
                stack.append((node.left, path+"L"))
            
        return src_path, dest_path
        
    def solution_1435_5_2(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path_s, path_d = self.solution_1435_5_1(root, startValue, destValue)
        
        i = j = 0
        while i < len(path_s) and j < len(path_d):
            if path_s[i] != path_d[j]:
                break
            i += 1
            j += 1
        
        return 'U' * len(path_s[i:]) + path_d[j:]