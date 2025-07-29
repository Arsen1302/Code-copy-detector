class Solution:
    def solution_1654_5(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        gr, gc = defaultdict(set), defaultdict(set)
        dr, dc = defaultdict(int), defaultdict(int)

        for a, b in rowConditions:
            if b in gr[a]: continue #drop duplicates
            gr[a].add(b)
            dr[b] += 1

        for a, b in colConditions:
            if b in gc[a]: continue
            gc[a].add(b)
            dc[b] += 1
        # start from leftmost and upmost nodes    
        row_start = [i for i in range(1, k+1) if not dr[i]]
        col_start = [i for i in range(1, k+1) if not dc[i]]
        if not row_start or not col_start:
            return []
        # row and col locations for nodes
        r, c = defaultdict(lambda: -1), defaultdict(lambda: -1)
        
        cnt = 0
        while row_start:
            q = []
            for x in row_start:
                r[x] = cnt
                cnt += 1
                for nei in gr[x]:
                    dr[nei] -= 1
                    if not dr[nei]:
                        q.append(nei)
            row_start = q
        # if still nodes with degree above zero, then cycle detected
        # e.g. [[1, 4], [4, 2], [2, 3], [3, 4]]
        if any(dr[x] for x in dr): return []
            
        cnt = 0
        while col_start:
            q = []
            for x in col_start:
                c[x] = cnt
                cnt += 1
                for nei in gc[x]:
                    dc[nei] -= 1
                    if not dc[nei]:
                        q.append(nei)
            col_start = q        
        
        if any(dc[x] for x in dc): return []
        
        non_used_row, non_used_col = len(r), len(c)  # for undefined nodes pick any unused row/cols     
        ans = [[0] * k for _ in range(k)]
        
        for i in range(1, k+1):
            x, y = None, None
            if r[i] != -1:
                x = r[i]
            else:
                x = non_used_row
                non_used_row += 1
            if c[i] != -1:
                y = c[i]
            else:
                y = non_used_col
                non_used_col += 1
            ans[x][y] = i
        
        return ans