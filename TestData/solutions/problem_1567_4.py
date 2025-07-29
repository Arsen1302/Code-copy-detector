class Solution:
  def solution_1567_4(self, tiles: List[List[int]], carpetLen: int) -> int:
    if carpetLen == 1 : return 1
    tiles.sort()
   
    ans = i = j = tmp = 0
    
    while ans != carpetLen :
      end = tiles[i][0] + carpetLen - 1 
      while j != len(tiles) and tiles[j][1] <= end:
        tmp += tiles[j][1] - tiles[j][0] + 1
        j += 1
      
      if j == len(tiles) : return max(ans, tmp)
       
      if end >= tiles[j][0] : ans = max(ans, tmp + min(end, tiles[j][1]) - tiles[j][0] + 1)
      else :ans = max(ans, tmp)
      
      if tmp == 0 : j += 1
      else : tmp -= (tiles[i][1] - tiles[i][0] + 1)
      i += 1
           
    return ans