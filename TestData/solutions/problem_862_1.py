class Solution:
    def solution_862_1(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = [id]
        count = 0
        seen = set(queue)
        while queue and count < level: #bfs
            count += 1
            temp = set()
            for i in queue: 
                for j in friends[i]:
                    if j not in seen: 
                        temp.add(j)
                        seen.add(j)
            queue = temp
        
        movies = dict()
        for i in queue: 
            for m in watchedVideos[i]: 
                movies[m] = movies.get(m, 0) + 1
        return [k for _, k in sorted((v, k) for k, v in movies.items())]