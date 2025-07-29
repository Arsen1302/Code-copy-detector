class Solution:
    def solution_1555_4(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        # make the grid which cells are guarded
        unseen = [[1]*n for _ in range(m)]

        # initialize a the number of unseen cells
        result = m*n

        # set all the walls and guards
        for rx, cx in walls + guards:

            # place the wall
            unseen[rx][cx] = 0

            # subtract from result
            result -= 1
        
        # now go over all the guards and update result
        # grx is guard row index
        # gcx is guard column index
        # brx is "blick" row index (blick is german for view)
        # bcx is "blick" column index
        for grx, gcx in guards:

            # go from this position till the left end or until we hit a wall
            for bcx in range(gcx-1, -1, -1):

                # check whether we change an unseen box
                if unseen[grx][bcx] == 1:
                    unseen[grx][bcx] = -1
                    result -= 1
                
                # check whether we hit a wall or other guard
                elif unseen[grx][bcx] == 0:
                    break
            
            # go from this position to the right end or wall
            for bcx in range(gcx+1, n):
                
                # check whether we change an unseen box
                if unseen[grx][bcx] == 1:
                    unseen[grx][bcx] = -1
                    result -= 1
                
                # check whether we hit a wall or other guard
                elif unseen[grx][bcx] == 0:
                    break
            
            # go from this position up and check for end or walls
            for brx in range(grx-1, -1, -1):
                
                # check whether we change an unseen box
                if unseen[brx][gcx] == 1:
                    unseen[brx][gcx] = -1
                    result -= 1
                
                # check whether we hit a wall or other guard
                elif unseen[brx][gcx] == 0:
                    break
                
            # go from this position down and check for end or walls
            for brx in range(grx+1, m):
                
                # check whether we change an unseen box
                if unseen[brx][gcx] == 1:
                    unseen[brx][gcx] = -1
                    result -= 1
                
                # check whether we hit a wall or other guard
                elif unseen[brx][gcx] == 0:
                    break
        return result