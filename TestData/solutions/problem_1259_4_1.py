class Solution:
    def solution_1259_4_1(self, num: str, k: int) -> int:
        import random
        
        class ImplicitTreap:
            class ImplicitTreapNode:
                def solution_1259_4_2(self, y, value, left=None, right=None):
                    self.y = y
                    self.value = value
                    self.left = left
                    self.right = right
                    self.size = 1
                
                def solution_1259_4_3(self):
                    self.size = (self.left.size if self.left is not None else 0) + (self.right.size if self.right is not None else 0) + 1
            
            def solution_1259_4_2(self, values=None):                
                self.root = None
                for value in values:
                    self.solution_1259_4_8(value)
            
            @staticmethod
            def solution_1259_4_4(left, right):
                if left is None:
                    return right
                if right is None:
                    return left
                
                if left.y > right.y:
                    left.right = ImplicitTreap.solution_1259_4_4(left.right, right)
                    result = left
                else:
                    right.left = ImplicitTreap.solution_1259_4_4(left, right.left)
                    result = right
                
                result.solution_1259_4_3()
                return result
            
            @staticmethod
            def solution_1259_4_5(node, index):
                if node is None:
                    return None, None
                
                left_size = node.left.size if node.left is not None else 0
                if index >= left_size + 1:
                    left, right = ImplicitTreap.solution_1259_4_5(node.right, index - left_size - 1)
                    node.right = left
                    node.solution_1259_4_3()
                    return node, right
                else:
                    left, right = ImplicitTreap.solution_1259_4_5(node.left, index)
                    node.left = right
                    node.solution_1259_4_3()
                    return left, node
                
            def solution_1259_4_6(self, index):
                if self.root is None or index > self.root.size or index < -self.root.size:
                    raise Exception('Index out of range')
                if index < 0:
                    index = -1 - index
                
                node = self.root
                while True:
                    left_size = node.left.size if node.left is not None else 0
                    if index < left_size:
                        node = node.left
                    elif node.left is not None and index == 0:
                        return node.value
                    elif index == left_size:
                        return node.value
                    else:
                        node = node.right
                        index -= left_size + 1
        
            def solution_1259_4_7(self, index, value):
                if self.root is None:
                    self.root = ImplicitTreap.ImplicitTreapNode(random.random(), value)
                    return
                
                if index > self.root.size:
                    raise Exception('Index out of range')
                
                left, right = ImplicitTreap.solution_1259_4_5(self.root, index)
                node = ImplicitTreap.ImplicitTreapNode(random.random(), value)
                self.root = ImplicitTreap.solution_1259_4_4(ImplicitTreap.solution_1259_4_4(left, node), right)
            
            def solution_1259_4_8(self, value):
                self.solution_1259_4_7(self.root.size if self.root is not None else 0, value)
            
            def solution_1259_4_9(self, index=None):
                if index is None:
                    index = self.root.size - 1
                
                left, right = ImplicitTreap.solution_1259_4_5(self.root, index)
                _, right = ImplicitTreap.solution_1259_4_5(right, 1)
                self.root = ImplicitTreap.solution_1259_4_4(left, right)
            
            def solution_1259_4_10(self):
                return self.root.size if self.root is not None else 0
            
            def solution_1259_4_11(self):
                result = []
                def solution_1259_4_12(node):
                    nonlocal result
                    if node is None:
                        return
                    
                    solution_1259_4_12(node.left)
                    result.solution_1259_4_8(node.value)
                    solution_1259_4_12(node.right)
                solution_1259_4_12(self.root)
                return str(result)
        
        
        def solution_1259_4_13(permutation):
            for i in range(len(permutation)-2, -1, -1):
                if permutation[i] < permutation[i+1]:
                    k = i
                    break
            else:
                return
            
            for i in range(len(permutation)-1, k, -1):
                if permutation[k] < permutation[i]:
                    r = i
                    break
            
            permutation = list(permutation)
            permutation[k], permutation[r] = permutation[r], permutation[k]
            return ''.join(permutation[0:k+1] + list(reversed(permutation[k+1:])))
        
        permutation = num
        for _ in range(k):
            permutation = solution_1259_4_13(permutation)
        
        result = 0
        permutation = ImplicitTreap(permutation)
        for i in range(len(permutation)):
            if num[i] != permutation[i]:
                for j in range(i+1, len(permutation)):
                    if num[i] == permutation[j]:
                        result += j - i 
                        permutation.solution_1259_4_9(j)
                        permutation.solution_1259_4_7(i, num[i])
                        break
        return result