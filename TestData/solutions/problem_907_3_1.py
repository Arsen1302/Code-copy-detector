class Solution:
    def solution_907_3_1(self, head: ListNode, root: TreeNode) -> bool:
        return self.solution_907_3_2(head, root)

    def solution_907_3_2(self, head: ListNode, root: TreeNode) -> bool:
        target_path = ''
        while head:
            target_path += f'|{head.val}'
            head = head.next

        path = ['']

        def solution_907_3_2(node: TreeNode) -> bool:
            ''' retval: is target found? '''
            if node:
                path.append(f'{path[-1]}|{node.val}')

                # check target
                if target_path in path[-1]: return True

                if solution_907_3_2(node.left): return True
                if solution_907_3_2(node.right): return True

                path.pop()  # recover
            return False

        return solution_907_3_2(root)