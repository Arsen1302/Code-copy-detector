class Solution:
	def solution_1723_5_1(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
		dic = {}
		inorder_array = []
		res = []
		def solution_1723_5_2(node):
			if(not node):
				return
			solution_1723_5_2(node.left)
			inorder_array.append(node.val)
			solution_1723_5_2(node.right)
    
		solution_1723_5_2(root)
		def solution_1723_5_3(target):
			start = 0
			end = len(inorder_array) - 1
			mid = 0
			while(start <= end):
				mid = (start + end) // 2
				if(inorder_array[mid] == target): #if target in the tree
					return [target, target]
				elif(inorder_array[mid] > target):
					end = mid - 1
				else:
					start = mid + 1
			#target not in the tree and then solution_1723_5_3 the interval of this target
			if(inorder_array[mid] > target): 
				if(mid != 0):
					return [inorder_array[mid - 1], inorder_array[mid]]
				else:
					return [-1, inorder_array[mid]] #target is at index 0 
			else:
				if(mid != len(inorder_array) - 1):
					return [inorder_array[mid], inorder_array[mid + 1]]
				else:
					return [inorder_array[mid], -1] #target is at last index
		for i in queries:
			res.append(solution_1723_5_3(i))
		return res