class Solution:
    def solution_862_4_1(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        def solution_862_4_2(a,b):
            if a[1] > b[1]:
                return 1
            elif a[1] < b[1]:
                return -1
            else:
                if a[0] > b[0]:
                    return 1
                else:
                    return -1
        vis = set()
        freq = defaultdict(int)
        pq = [[0,id]]
        while pq:
            dist,node = heappop(pq)
            if node not in vis:
                if dist == level:
                    for videos in watchedVideos[node]:
                        freq[videos]+=1
                else:
                    for it in friends[node]:
                        heappush(pq,[dist+1,it])
                vis.add(node)
        sorted_keys = sorted(freq.items(),key = cmp_to_key(solution_862_4_2))
        ans = [key[0] for key in sorted_keys]
        return ans