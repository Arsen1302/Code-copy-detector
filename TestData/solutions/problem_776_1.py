class Solution:
    def solution_776_1(self, root: TreeNode) -> int:
        
        queue = deque() #init a queue for storing nodes as we traverse the tree
        queue.append(root) #first node (level = 1) inserted
        
        #bfs = []  #just for understanding- this will be a bfs list to store nodes as we conduct the search, but we don't need it here.
        
        level_sum = 0 # for sum of each level
        level_nodes = 1 # for knowing when a particular level has ended
        
        sum_of_levels = [] #list to store all levels sum of nodes
        
        while queue: #begin BFS
            node = queue.popleft() 
            #bfs.append(node)
            level_sum += node.val #add node 
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
            level_nodes -= 1   #reduce level number by 1, as we popped out a node
            if level_nodes == 0: # if 0, then a level has ended, so calculate the sum
                sum_of_levels.append(level_sum)
                level_sum = 0
                level_nodes = len(queue)
        
        return sum_of_levels.index(max(sum_of_levels)) + 1  #return index of max level sum