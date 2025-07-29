class Solution:
    def solution_639_4(self, root: TreeNode) -> bool:
        i = -1
        prev = 1/2
        queue = [root]
        while queue: 
            newq = []
            flag = False
            if prev != 2**i: return False # check previous level is full 
            for node in queue: 
                for child in (node.left, node.right): 
                    if child: 
                        if flag: return False
                        else: newq.append(child)
                    else: flag = True 
            i += 1
            prev = len(queue)
            queue = newq
        return True