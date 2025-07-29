class Solution:
    def solution_916_4_1(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
        # connections
        self.conn = collections.defaultdict(list)
        
        # get the connections
        for edge in edges:
            self.conn[edge[0]].append(edge[1])
            self.conn[edge[1]].append(edge[0])
            
        # safe the probability
        self.prob = 0
        
        # make an array for the visited nodes
        # since these are only identified by
        # an increasing int, we can use an array
        # of bools
        self.visited = [False]*n
        self.visited[0] = True
        
        # make a solution_916_4_2 - during solution_916_4_2 we always will
        # add probability of path if we found a valid
        # one
        self.solution_916_4_2(1, 1, t, target)
        
        return self.prob
        
    def solution_916_4_2(self, current, prob, time, target):

        # if time is over we need to check
        # whether we are at the target
        # otherwise we just return
		# -> stop condition 3b
        if time == 0:
            if current == target:
                self.prob += prob
            return

        # get the current nodes we can visit
        visible = self.conn[current]

        # get the amount of nodes we can
        # visit and have not already visited
        amount = 0
        for node in visible:

            # guard clause if we visited the node
            if self.visited[node-1]:
                continue

            # increase the amount of nodes we can visit
            amount += 1

        # check whether we can visit any nodes
        if amount:
            
            # check whether we are at target and therefore target is out
			# stop condition 3c
            if current == target:
                return
            
            # calculate the updated probability and time
            updated_time = time-1
            updated_probability = prob*(1/amount)

            # go through all nodes we have not visited
            for node in visible:

                # guard clause to skip nodes we have visited
                if self.visited[node-1]:
                    continue

                # set the current node as visited
                self.visited[current-1] = True

                # traverse further and with updated values
                self.solution_916_4_2(node, updated_probability, updated_time, target)

                # reset that we visited this node
                self.visited[current-1] = False

        # we can not visit any further nodes
		# stop condition 3a
        else:
            
            # check whether we are at target
            if current == target:
                self.prob += prob


        return