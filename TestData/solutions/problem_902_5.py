class Solution:
    def solution_902_5(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        child = set()
        parent = set()
        
        for i in range(len(leftChild)):
            if (leftChild[i] != -1 and leftChild[i] in child) or (rightChild[i] != -1 and rightChild[i] in child):
                return False
            if i in child and ((leftChild[i] != -1 and leftChild[i] in parent) or (rightChild[i] != -1 and rightChild[i] in parent)):
                return False
            
            if leftChild[i] != -1:
                child.add(leftChild[i])
            if rightChild[i] != -1:
                child.add(rightChild[i])
            
            parent.add(i)
        
        if len(child) != len(leftChild) - 1:
            return False
        
        return True