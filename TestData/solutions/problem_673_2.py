class Solution:
    def solution_673_2(self, root: TreeNode, x: int, y: int) -> bool:
        q = [root]
        while(q):
            toggle = 0
            parents = []
            for i in range(len(q)): # Level wise exploration starts here
                temp = q[0] # storing the first element in a temp variable
                q.pop(0) # Dequeuing the first element and exploring its neighbours below
                if(temp.left):
                    q.append(temp.left)
                    if(temp.left.val==x or temp.left.val==y):
                        toggle += 1
                        parents.append(temp)
                if(temp.right):
                    q.append(temp.right)
                    if(temp.right.val==x or temp.right.val==y):
                        toggle += 1
                        parents.append(temp)
			# Level wise exploration ends here
            # if toggle == 2 that means both x and y are on same level/depth
            if((toggle==2) and (parents[0] != parents[1])):
                return True # x and y are cousins
        return False