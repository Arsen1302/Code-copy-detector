class Solution:
    import heapq
    def solution_116_1_1(self, root: Optional[TreeNode], k: int) -> int:
        
        heap = []
        def solution_116_1_2(r):
            if r:
                solution_116_1_2(r.left)
                heapq.heappush(heap,-(r.val))
                if len(heap) > k:
                    heapq.heappop(heap)
                solution_116_1_2(r.right)
        solution_116_1_2(root)
        
        return -heapq.heappop(heap)