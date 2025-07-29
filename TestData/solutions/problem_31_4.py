class Solution:
    def solution_31_4(self, numRows: int) -> List[List[int]]:
		triangle = []          #initiating the triangle which we will output
		
		for row_num in range(numRows):            # for loop for adding rows to the final triangle
            row = [None for _ in range(row_num + 1)]  #intiating each row with None, notice the no. of elements in the row
			row[0], row[-1] = 1, 1        #first and last element of each row is 1
			
            for j in range(1, row_num):     # nested for loop to fill up each row
                row[j] = triangle[row_num - 1][j-1] + triangle[row_num - 1][j]   #as seen in question animation, each element is the sum of the elements directly above it
				
            triangle.append(row)  #After filling up the row - append it to the main traingle
			
        return triangle   #return the triangle