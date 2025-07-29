class Solution:
    def solution_902_3(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Get all the children in the tree
        childs = set(leftChild + rightChild)
        root = 0
        # The element which is not in childs set is the root element
        for i in range(n):
            if i not in childs:
                root = i
                break
        # Do a BFS on the tree and keep track of nodes we visit
        visited = []
        queue = [root]
        while queue:
            ele = queue.pop(0)
            # If the element is already visited, it means it's not a tree
            if ele in visited:
                return False
            
            visited.append(ele)
            # If node has left child, add it to queue
            if leftChild[ele] != -1:
                queue.append(leftChild[ele])
            # If node has right child, add it to queue
            if rightChild[ele] != -1:
                queue.append(rightChild[ele])
                
        # At the end, if all the nodes (n) are visited, it means it's a tree
        return len(visited) == n