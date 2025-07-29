class Solution:
    def solution_737_2_1(self, tiles: str) -> int:
        ds=[]
        self.ans=set()
        self.solution_737_2_2(tiles,ds)
        return len(self.ans)
    def solution_737_2_2(self,tiles,ds):
        for i in range(len(tiles)):
            ds.append(tiles[i])
            self.ans.add("".join(ds[:]))
            self.solution_737_2_2(tiles[:i]+tiles[i+1:],ds)
            ds.pop()
        return