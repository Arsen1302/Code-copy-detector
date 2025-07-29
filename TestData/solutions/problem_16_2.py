class Solution:
    def solution_16_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res = []
        q = deque()
        q.append(root)
        switch = False  #check if we need to reverse in that layer 
        
        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
			
            if switch: # need to reverse the order in this layer
                tmp.reverse()
            res.append(tmp)
			# remember to turn on and off
            switch = not switch
        return res