class Solution:
    def solution_907_1_1(self, head: ListNode, root: TreeNode) -> bool:
        #build longest prefix-suffix array
        pattern, lps = [head.val], [0] #longest prefix-suffix array
        j = 0
        while head.next: 
            head = head.next 
            pattern.append(head.val)
            
            while j and head.val != pattern[j]: j = lps[j-1]
            if head.val == pattern[j]: j += 1
            lps.append(j)
            
        def solution_907_1_2(root, i): 
            """Return True of tree rooted at "root" match pattern"""
            if i == len(pattern): return True
            if not root: return False 
            
            while i > 0 and root.val != pattern[i]: i = lps[i-1]
            if root.val == pattern[i]: i += 1
            return solution_907_1_2(root.left, i) or solution_907_1_2(root.right, i)
        
        return solution_907_1_2(root, 0)