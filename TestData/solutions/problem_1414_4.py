class Solution:
    def solution_1414_4(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for outgoing, incoming, distance in edges:
            graph[outgoing].append((incoming, distance))
            graph[incoming].append((outgoing, distance))
        # At each node, we have at most four possible moves
        # dp[loc][maxTime] = max(*[dp[adj][maxTime - dist(adj)] for adj in adjs], value[loc])

        # as many unique nodes as possible..
        # able to return to start
        # maximize value

        # compute shortest path from all nodes to 0
        # dijktra
        distance_to_origin = defaultdict(lambda: inf)
        distance_to_origin[0] = 0
        visited = set()
        to_visit = [(0, 0)]
        while len(to_visit) > 0:
            dist, cur = heappop(to_visit)
            if cur in visited or dist != distance_to_origin[cur]:
                continue
            for neighbor, distance in graph[cur]:
                if distance_to_origin[cur] + distance < distance_to_origin[neighbor]:
                    distance_to_origin[neighbor] = distance_to_origin[cur] + distance
                    heappush(to_visit, (distance_to_origin[neighbor], neighbor))
            visited.add(cur)

        #  start from 0, reach out (how to determine returnability?)
        # with the shortest path map, we can prune branches that cannot return to the start
        d = deque([(0, maxTime, set(), 0)])
        best = values[0]
        while len(d) > 0:
            for _ in range(len(d)):
                cur, time, unique, val = d.popleft()
                if cur == 0:
                    best = max(best, val)
                if distance_to_origin[cur] > time:
                    # no way home
                    continue
                for to, distance in graph[cur]:
                    if distance > time:
                        continue
                    new_val = values[to] + val if to not in unique else val
                    # Conditionally copy the unique set
                    new_unique = set(unique) | set([to]) if to not in unique else unique
                    d.append((to, time - distance, new_unique, new_val))
        return best