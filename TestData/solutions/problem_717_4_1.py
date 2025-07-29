class Solution:
    def solution_717_4_1(self, root: TreeNode) -> TreeNode:
        arr = []
        
        def solution_717_4_2(r):
            if r:
                solution_717_4_2(r.left)
                arr.append(r.val)
                solution_717_4_2(r.right)
        
        solution_717_4_2(root)
        
        d = defaultdict(int)
        
        tmp = 0
        for i in range(len(arr) - 1, -1, -1):
            tmp += arr[i]
            d[arr[i]] = tmp
        
        def solution_717_4_3(r):
            if r:
                solution_717_4_3(r.left)
                r.val = d[r.val]
                solution_717_4_3(r.right)
                
        solution_717_4_3(root)
        
        return root