class Solution:
    def solution_1630_2(self, edges: List[int]) -> int:
        res, seenSet = -1, set()
        for element in range(len(edges)): #traverses all possible nodes
            count, currNode = 0, element
            cycleMap = dict() #tabulates all distances
            while currNode not in seenSet and currNode != -1:
                count += 1
                seenSet.add(currNode); cycleMap[currNode] = count #adds nodes to the hashmap and the hashset
                currNode = edges[currNode] #moves on to the next node
            res = max(res, count + 1 - cycleMap.get(currNode, 200000)) #gets the max distance 
        return res