class Solution:
    def solution_324_3_1(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        def solution_324_3_2(u):
            if not visited[u]:
                visited[u] = True
                for i in range(n):
                    if isConnected[i][u]: #treveses all the conneted nodes
                        solution_324_3_2(i)
        ans = 0
        for i in range(n):
            if not visited[i]: #only traverses untravesed nodes
                solution_324_3_2(i)
                ans+=1
        return ans