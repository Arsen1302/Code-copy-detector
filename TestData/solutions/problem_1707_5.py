class Solution:
    def solution_1707_5(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d = {}
        max_views = 0

        for creator, view, id in zip(creators, views, ids):
            # views, max viewed, id
            if creator not in d:
                d[creator] = [0, view, id]  
            elif view == d[creator][1]:
                d[creator][2] = id if id < d[creator][2] else d[creator][2]
            elif view > d[creator][1]:
                d[creator][1] = view
                d[creator][2] = id
            
            d[creator][0] += view
            if d[creator][0] > max_views:
                max_views = d[creator][0]
        
        res = []
        for k, v in d.items():
            if v[0] == max_views:
                res.append([k, v[2]])
        
        return res