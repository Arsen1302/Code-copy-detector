class Solution:
    def solution_527_5_1(self, strs: List[str]) -> int:
        def solution_527_5_2(word1, word2):
            diff = []
            for a,b in zip(word1, word2):
                if a != b:
                    diff.append((a,b))
                    if diff and len(diff) > 2:
                        return False
            if diff and sorted(diff[0]) != sorted(diff[1]):
                return False
            return True
        
        graph = {}
        for i in range(len(strs)):
            graph[strs[i]] = []
            for j in range(len(strs)):
                if i != j and solution_527_5_2(strs[i], strs[j]):
                    graph[strs[i]].append(strs[j])
        # print(graph)
        
        visited = set()
        q = deque()
        group_count = 0
        for i in range(len(strs)):
            if strs[i] not in visited:
                group = []
                q.append(strs[i])
                while q:
                    node = q.popleft()
                    visited.add(node)
                    group.append(node)
                    for sim in graph[node]:
                        if sim not in visited:
                            q.append(sim)
                # print(group, visited)
                group_count += 1
        return group_count