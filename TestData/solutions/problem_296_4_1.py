class Solution:
    def solution_296_4_1(self, root: Optional[TreeNode]) -> List[int]:
        
        hashmap = defaultdict(int)
            
        def solution_296_4_2(root):
            
            nonlocal hashmap
        
            if not root:
                
                return 0
            
            left = solution_296_4_2(root.left)
            
            right = solution_296_4_2(root.right)
            
            subtree_sum = root.val + left + right
            
            hashmap[subtree_sum] += 1
            
            return subtree_sum
        
        solution_296_4_2(root)
        
        curr_max = -1
        
        ret = list()
        
        #maxi = max(hashmap.values()) 0(n where n is number of elements)
        
        #return [ele for ele in hashmap if hashmap[ele] == maxi] 0(n)
        
        for ele in hashmap:
            
            if hashmap[ele] == curr_max:
                ret.append(ele)
                
            
            elif hashmap[ele] > curr_max:
                
                curr_max = hashmap[ele]
                ret = [ele]
            
        return ret