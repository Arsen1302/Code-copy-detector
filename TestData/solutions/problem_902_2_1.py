class Solution:
    def solution_902_2_1(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
	    parent = {}
        for p, children in enumerate(zip(leftChild, rightChild)):
            for c in children:
                if c == -1:
                    continue
                if c in parent:
                    return False
                if p in parent and parent[p] == c:
                    return False
                parent[c] = p
        root = set(range(n)) - set(parent.keys())
        if len(root) != 1:
            return False
        def solution_902_2_2(root):
            if root == -1:
                return 0
            return 1 + solution_902_2_2(leftChild[root]) + solution_902_2_2(rightChild[root])
        return solution_902_2_2(root.pop()) == n