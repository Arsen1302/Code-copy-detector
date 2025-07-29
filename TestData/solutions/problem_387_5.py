class Solution:
    def solution_387_5(self, root: Optional[TreeNode]) -> int:
        queue=[[root,0]]
        m=0
        while(queue):
            m=max(m,queue[-1][1]-queue[0][1])
            for i in range(len(queue)):          
                node,cur=queue.pop(0)
                if(node.left):  queue.append([node.left,2*cur+1])
                if(node.right): queue.append([node.right,2*cur+2])
        return m+1