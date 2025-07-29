class Solution:
    def solution_1636_2(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        #Convert restricted list into restricted set to increase processing speed
        #Create a dictionary of non-restricted nodes 
        #Thus the key is the node and the value is the adjacency set for that node
        resSet = set(restricted)        
        nodes_dict = dict()     
        for x in range(0, n):
            if(x not in resSet):
                nodes_dict[x] = set()

        #Fill adjacency set only with non-restricted nodes
        #We can check for non-restricted nodes by using the keys of the dict
        for pair0, pair1 in edges:
            if(pair0 in nodes_dict and pair1 in nodes_dict):
                nodes_dict[pair0].add(pair1)
                nodes_dict[pair1].add(pair0)

        #We will always start at node 0, so I add 0 to the traversalQueue
        #Add 0 to counting set since we always have 0
        traversalQueue = deque([0])
        count = {0}

        #Utilize set operations
        #Starting at 0 look at 0's adjacency set
        #Use difference operation to find which of 0's neighbors are not visited to add to the traversalQueue
        #####
        #Obviously none of 0's neighbors have been visited but...
        #...for rest of the nodes, you don't want to traverse backwards and get stuck
        #The reason why you will get stuck if you don't do the difference operation is because:
        #The edge comes in pairs. So [0,1] means that 0 will have 1 in its adjacency set. However...
        #...1 will also have 0. If you do not account for this, when you get to node 1 in the dict...
        #...all of 1's neighbors INCLUDING 0 will be added to the traversalQueue. Thus an infinite loop occurs.
        #####
        #Add the neighbors to the traversalQueue
        #Add all neighbors to counting set
        #Remove node from traversalQueue FIFO style. At the start that will obviously be node 0.
        #Repeat until you have traversed all nodes
        while(len(traversalQueue) != 0):
            current = traversalQueue[0]
            diff = nodes_dict[current].difference(count)
            traversalQueue.extend(diff)
            count.update(diff)
            traversalQueue.popleft()

        return len(count)