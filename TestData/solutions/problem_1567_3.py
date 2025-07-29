class Solution:
    def solution_1567_3(self, tiles: List[List[int]], carpetLength: int) -> int:
        n=len(tiles)
        tiles.sort(key=lambda x:x[0]) #sorting on starting point
        i,j,whiteMarbel,ans=[0]*4
        while i<n:
            nextStartingPoint=tiles[i][0]+carpetLength #carpet will cover till nextStartingPoint-1.
            partial=0
            while j<n and tiles[j][1]<nextStartingPoint:
                whiteMarbel+=tiles[j][1]-tiles[j][0]+1 #storing all whitemarbels which are covered by carpet.
                j+=1
            if j<n:
                partial=max(0,nextStartingPoint-tiles[j][0]) #if current laid carpet overlap with partial interval
            ans=max(ans,whiteMarbel+partial) #calculating max value 
            whiteMarbel-=tiles[i][1]-tiles[i][0]+1 #removing value at ith index as we are sliding starting point of carpet to next index
            i+=1
        return ans