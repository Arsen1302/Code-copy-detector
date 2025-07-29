class Solution:
    def solution_296_5_1(self, root: Optional[TreeNode]) -> List[int]:
        # Stores count of solution_296_5_2 sum
        # hash_map[2] = 4 ==> substree sum 2 have frequency of 4
        hash_map = {}
        
        def solution_296_5_2(root):
            if not root:
                return 0
            
            left_subtree = solution_296_5_2(root.left)
            right_subtree = solution_296_5_2(root.right)
			# Subtree sum is root +  left + right
            sum_subtree = root.val + left_subtree + right_subtree
			# Whenever we get same solution_296_5_2 sum, increment the count
            hash_map[sum_subtree] = hash_map.get(sum_subtree, 0) + 1
            
            return sum_subtree
        
        solution_296_5_2(root)
        max_sum = max(list(hash_map.values()))
        res = []
        return [k for k, v in hash_map.items() if v == max_sum]