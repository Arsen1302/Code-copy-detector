class Solution:
    def solution_1401_5_1(self, parents: List[int]) -> int:
        n = len(parents)
        
        dic = {} # parent : sons
        for i in range(n):
            if parents[i] not in dic:
                dic[parents[i]] = []
            dic[parents[i]].append(i)
        
        # dfs solution_1401_5_2 the size of each node (number of subtrees + node itself)
        # save the result in tree_size
        tree_size = [0 for i in range(n)]
        def solution_1401_5_2(root: int):
            root_size = 1
            if root in dic: # if root is a parent
                for son in dic[root]:
                    son_size = solution_1401_5_2(son)
                    root_size += son_size
            
            tree_size[root] = root_size
            return root_size
        
		# solution_1401_5_2 the root
        solution_1401_5_2(0)
        
        max_score = 0
        freq = {}
        for i in range(n):
			# initialization: if i is not a parent
            left_size = 0
            right_size = 0
            
            if i in dic: # if i is a parent
                if len(dic[i]) > 0:
                    left_size = tree_size[dic[i][0]] # size of its left subtree
                if len(dic[i]) > 1:
                    right_size = tree_size[dic[i][1]] # size of its right subtree
                    
            # score = size of left subtree * size of right subtree * size the other trees (except i which is removed)
            score = max(left_size, 1) * max(right_size, 1) * max(n - 1 - left_size - right_size, 1)
            
            if score not in freq:
                freq[score] = 0
            freq[score] += 1
            max_score = max(max_score, score)
            
        return freq[max_score]