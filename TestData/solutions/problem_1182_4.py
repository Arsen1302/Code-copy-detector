class Solution:
    def solution_1182_4(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        # make the connections
        conns = collections.defaultdict(set)
        
        # connect the connections
        for a, b in adjacentPairs:
            conns[a].add(b)
            conns[b].add(a)
            
        # find the start value
        for node, conn in conns.items():
            if len(conn) == 1:
                break
        
        # remove the first node from the first connection
        result = [node]
        while conns[node]:
            
            # get the next element
            # (there can only be one, as we always remove one)
            new = conns[node].pop()
            
            # append the new element to the list
            result.append(new)
            
            # delete node from the next connections
            conns[new].remove(node)
            
            # set the new element
            node = new
        return result