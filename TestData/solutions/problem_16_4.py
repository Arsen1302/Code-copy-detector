class Solution:
	def solution_16_4(self, root: TreeNode) -> List[List[int]]:
		if not root:
			return
		d=[]
		l=[]
		d.append(root)
		p=0
		direction=1
		while d:
			q=len(d)
			l1=[]
			while q:
				i=d.pop(0)
				l1.append(i.val)
				if i.left:
					d.append(i.left)
				if i.right:
					d.append(i.right)
				q-=1
			l.append((l1)[::direction])
			direction=direction*-1
		return l