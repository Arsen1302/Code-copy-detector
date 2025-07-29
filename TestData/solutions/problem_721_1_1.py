class Solution:
    def solution_721_1_1(self, N: int, paths: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for path in paths:
            G[path[0]].append(path[1])
            G[path[1]].append((path[0]))
        colored = defaultdict()

        def solution_721_1_2(G, V, colored):
            colors = [1, 2, 3, 4]
            for neighbour in G[V]:
                if neighbour in colored:
                    if colored[neighbour] in colors:
                        colors.remove(colored[neighbour])
            colored[V] = colors[0]

        for V in range(1, N + 1):
            solution_721_1_2(G, V, colored)

        ans = []
        for V in range(len(colored)):
            ans.append(colored[V + 1])

        return ans