class Solution:
    def solution_1724_5_1(self, roads: List[List[int]], seats: int) -> int:

        # we can do solution_1724_5_2 into the leaf nodes and on return calculate the
        # amount of people that travel together. We will travel to the
        # leaves first and count the collected representatives on the
        # way back. During that we also continously add the fuel needed
        # to travel from node to next node closer to root.

        # make the graph for all of the roads in order to have a quick
        # lookup
        graph = collections.defaultdict(list)
        for start, end in roads:
            graph[start].append(end)
            graph[end].append(start)
        
        # make a instance variable to count the fuel
        self.fuel = 0

        # start the depth first approach
        self.solution_1724_5_2(0, -1, graph, seats)

        # return our result
        return self.fuel

    def solution_1724_5_2(self, position, parent, graph, seats):
        
        # go deeper into the graph for all connections still open and
        # add up the representatives travelling to our node. Do not
        # forget to start at one representative, as our node also 
        # has an representative
        representatives = 1
        for target in graph[position]:

            # check that we do not go back in root direction
            if target != parent:

                # count the representatives coming from nodes deeper in the
                # tree
                representatives += self.solution_1724_5_2(target, position, graph, seats)
        
        # get the fuel costs for each car of collected representatives, but
        # take care to not travel further once we are at root node ( position == 0)
        if position > 0:
            
            # calculate the number of cars we need to go further
            # this is just a quick way of saying: math.ceil(representatives/2)
            self.fuel += (representatives + seats-1) // seats

        # go in the the root node direction and hand over the number of incoming
        # representatives
        return representatives