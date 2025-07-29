class Solution:
    def solution_681_4_1(self,row,col):
        return 1 if (self.rows[row] > 0 or self.cols[col] > 0 \
        or self.digonal1[row-col] > 0 or self.digonal2[row+col] > 0) else 0
    
    def solution_681_4_2(self,row,col):
        adj = ((row,col),(row+1,col),(row-1,col),(row,col-1),(row,col+1),\
              (row+1,col-1),(row+1,col+1),(row-1,col-1),(row-1,col+1))
        for xy in adj:
            if xy in self.origin:
                self.rows[xy[0]] -= 1
                self.cols[xy[1]] -= 1
                self.digonal1[xy[0]-xy[1]] -= 1
                self.digonal2[xy[0]+xy[1]] -= 1
                self.origin.pop(xy)

    def solution_681_4_3(self,row,col):
        self.rows[row] += 1
        self.cols[col] += 1
        self.digonal1[row-col] += 1
        self.digonal2[row+col] += 1
        
                
    def solution_681_4_4(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.digonal1 = defaultdict(int)
        self.digonal2 = defaultdict(int)
        self.origin = {}
        ans = []
        for r,c in lamps: 
            if (r,c) not in self.origin:
                self.origin[(r,c)] = True        
                self.solution_681_4_3(r,c)
        for r,c in queries:
            ans.append(self.solution_681_4_1(r,c))
            self.solution_681_4_2(r,c)
        return ans