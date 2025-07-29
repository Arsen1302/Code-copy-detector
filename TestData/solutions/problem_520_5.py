class Solution:
   def solution_520_5(self, image: List[List[int]]) -> List[List[int]]:
       result = []
       for i in range(len(image)):
           for j in range(len(image[i])):
               if image[i][j] == 1:
                   image[i][j] = 0
               else:image[i][j] = 1
           result.append(image[i][::-1])
       return result