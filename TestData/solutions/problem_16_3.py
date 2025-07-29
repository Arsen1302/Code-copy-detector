class Solution:
    def solution_16_3(self, root: TreeNode) -> List[List[int]]:
        if root== None:
            return []
        else:
            res = []
            queue = []
            queue.append(root)
            flag = True
            while queue:
                level = []
                flag = -flag
                for _ in range(len(queue)):
                    temp = queue.pop(0)
                    level.append(temp.val)
                    
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
                if flag == True:
                    level = level[::-1]
                res.append(level)
        return res