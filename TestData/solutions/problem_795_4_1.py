class Solution:
    def solution_795_4_1(self, s: str, pairs: List[List[int]]) -> str:
        def solution_795_4_2(idx, arr):
            arr.append(idx)
            visited[idx] = True
            for nei in graph[idx]:
                if not visited[nei]:
                    visited[nei] = True
                    solution_795_4_2(nei, arr)
            
        graph = collections.defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        n = len(s)
        s_list = list(s)
        visited = [False] * n
        for idx in range(n):
            if not visited[idx]:
                arr = []
                solution_795_4_2(idx, arr)
                arr.sort()
                letter = [s[i] for i in arr]
                letter.sort()
                for i in range(len(arr)):
                    s_list[arr[i]] = letter[i]
        return ''.join(s_list)