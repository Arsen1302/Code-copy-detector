class Solution:
    def solution_1720_5_1(self, root: Optional[TreeNode]) -> int:
        levels = []
        res = 0
        
        def solution_1720_5_2(node, level):
            if level >= len(levels):
                levels.append([])
            
            if node:
                levels[level].append(node.val)
                
                if node.left:
                    solution_1720_5_2(node.left, level + 1)
                if node.right:
                    solution_1720_5_2(node.right, level + 1)
        
        def solution_1720_5_3(nums):
            s = sorted(nums)
            dic = {}
            solution_1720_5_3 = 0
            
            for i, n in enumerate(nums): 
                dic[n] = i
            
            for i in range(len(nums)):
                if nums[i] != s[i]:
                    idx = dic[s[i]]     
                    dic[nums[i]] = idx
                    dic[s[i]] = i
                    nums[i], nums[idx] = nums[idx], nums[i]
                    solution_1720_5_3 += 1
                    
            return solution_1720_5_3
                        
        solution_1720_5_2(root,0)
        for i in range(len(levels)):
            res += solution_1720_5_3(levels[i])
        
        return res