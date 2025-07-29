class Solution:
    def solution_261_4_1(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        visited = [[0 for x in range(col)] for y in range(row)]
        
        def solution_261_4_2(i, j):
            # we're at a boundary node or a 0 node but we reached here
            # from a 1 node, so this "unwanted node" is a adjacent to one
            # of the wanted nodes and hence sharing the boundary (part perimeter)
            # add 1 to the perimeter here
            if i < 0 or i > row-1 or j < 0 or j > col-1 or grid[i][j] == 0:
                return 1
            
            # return if the current node is visited, we don't need
            # to count that as part of our permieter calculation
            # if not visited, mark the current node as visited,
            # this is a legit node
            if visited[i][j]:
                return 0
            visited[i][j] = 1
            
            # now recursively check all the neighbours of the current node
            return solution_261_4_2(i-1, j) + solution_261_4_2(i+1, j) + solution_261_4_2(i, j+1) + solution_261_4_2(i, j-1)
        
        # loop over all elements in the
        # matrix and as soon as you find
        # a piece of land(1); begin graph
        # traversal and we can safely return
        # here since it's going to traverse
        # the whole island and there's just 1
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    return solution_261_4_2(x, y)