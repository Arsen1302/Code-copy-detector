class Solution:
    def solution_1720_2_1(self,arr):
        
        n = len(arr)
        cnt = 0
        a = sorted(arr)
        index = {}
        
		# store index of elements in arr
        for ind in range(n):
            index[arr[ind]] = ind

        for ind in range(n):
			
			# If element in arr is out of position we need to swap hence increase cnt
            if (arr[ind] != a[ind]):
                cnt += 1
                pos = arr[ind]
                
				# Replace it with element that should be at this "ind" in arr using a[ind]
                arr[ind], arr[index[a[ind]]] = arr[index[a[ind]]], arr[ind]
				
				# Update the indexes for swaped elements in "index"
                index[pos] = index[a[ind]]
                index[a[ind]] = ind

        return cnt
    
    def solution_1720_2_2(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        q = [root]
        # Level order traversal
        while q :
            
            level = []
            values = []
            for n in q:
                
                if n.left :
                    level.append(n.left)
                    values.append(n.left.val)
                
                if n.right :
                    level.append(n.right)
                    values.append(n.right.val)
            
            res += self.solution_1720_2_1(values)
            q = level
        
        return res