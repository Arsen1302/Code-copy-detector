class Solution:
    def solution_1435_2(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
	
        graph=defaultdict(list)    
        stack=[(root)]
		
		#Step1: Build Graph
        while stack:
            node=stack.pop()
            
            if node.left:
                graph[node.val].append((node.left.val,"L"))
                graph[node.left.val].append((node.val,"U"))
                stack.append(node.left)
            if node.right:
                graph[node.val].append((node.right.val,"R"))
                graph[node.right.val].append((node.val,"U"))
                stack.append(node.right)
        #Step 2: Normal BFS
        q=deque([(startValue,"")])
        seen=set()
        seen.add(startValue)
        
        while q:
            node,path=q.popleft()
            if node==destValue:
                return path
            
            for neigh in graph[node]:
                v,d=neigh
                if v not in seen:
                    q.append((v,path+d))
                    seen.add(v)
        return -1