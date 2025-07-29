class Solution:
    def solution_1548_2_1(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for child,  par in enumerate(parent):
            tree[par].append(child)
            
        max_length = 1
        def solution_1548_2_2(node):
            nonlocal max_length
            if not tree[node]:
                return 1
            heap = [-1,-1]
            for child in tree[node]:
                if s[child] != s[node]:
                    heappush(heap,-1*(solution_1548_2_2(child) + 1))
                else:
                    solution_1548_2_2(child)
            first_max= -heappop(heap)
            second_max = -heappop(heap)
            cur_max = first_max + second_max - 1
            max_length = max(max_length,cur_max)
            
            return first_max
        solution_1548_2_2(0)
        return max_length