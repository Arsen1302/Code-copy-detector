class Solution(object):
    def solution_57_4(self, root):
        # Create an empty stack and push the root node...
        bag = [root]
        # Create an array list to store the solution result...
        sol = []
        # Loop till stack is empty...
        while bag:
            # Pop a node from the stack...
            node = bag.pop()
            if node:
                sol.append(node.val)
                # Append the right child of the popped node into the stack
                bag.append(node.right)
                # Push the left child of the popped node into the stack
                bag.append(node.left)
        return sol      # Return the solution list...