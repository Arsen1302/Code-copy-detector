class Solution:
    def solution_639_1(self, root: TreeNode) -> bool:
                        # The criteria for an n-level complete tree:
                        #
                        #   • The first n-1 rows have no null nodes.
                        #
                        #   • The nth row has no non-null nodes to the right of the left-most null
                        #     node encountered (if it exists).
                        #
                        # The plan is to bfs the tree, left to right, level by level. We mark the
                        # instance of the first null popped from the queue and then ensure the remaining
                        # queue is only null nodes. If so, both criteria are satisfied and True is
                        # returned. If not, False is returned.

        queue = deque([root])                       #   <-- initialize the queue

        while queue[0]:                             #   <-- if and while top queue node is not null, pop   
            node = queue.popleft()                  #       it and then push its left child and right  
            queue.extend([node.left, node.right])   #       child onto the queue.

        while queue and not queue[0]:               #   <-- if and while top queue node is null, pop it. 
            queue.popleft()                         #        

        if queue: return False                      #   <-- If the queue is not empty, it must be non-null, so 
        return True                                 #       return False; if the queue is empty, return True.