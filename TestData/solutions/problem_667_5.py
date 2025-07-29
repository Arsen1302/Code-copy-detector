class Solution(object):
    def solution_667_5(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        myC=defaultdict(list)  #key=col  value=[(row,node.val),...]
        
        stack=[(root,0,0)] #node, col, row
        maxCol,minCol=0,0  #the goal of this to avoid sorting the whole myC dictionary at the end 
        
        while stack:   #DFS O(N)
            node,col,row=stack.pop()
            maxCol,minCol=max(maxCol,col),min(minCol,col)  
            myC[col].append((row,node.val))  #append tuple to hashmap
            if node.left:
                stack.append((node.left,col-1,row+1)) #DFS: so row+1 and if left so col-1
            if node.right:
                stack.append((node.right,col+1,row+1)) #DFS: so row+1 and if right so col+1

        res=[]    
        for col in range(minCol,maxCol+1): #loop on range otherwise I would loop on sorted(myC) that will result in added complexity
            res.append([v for row,v in sorted(myC[col])])  #for loop is O(N), sorted is O(XlogX), what is X here, 
			#if we assume nodes are distributed on cols so each # of cols=K , so each col has N/k nodes,
			#so sorting 1 col is O(N/K log N/K), sorting K cols = O(NK/K log N/K) --> simplify = O(N log N/k)

        return res    #so total time = O(N) DFS + O(N) for loop + O(NlogN/K) = O(NlogN/K)   , while space=stack andhashmap = O(N)