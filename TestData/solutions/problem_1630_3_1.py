class Solution:
    def solution_1630_3_1(self, edges: List[int]) -> int:
        
        def solution_1630_3_2(i, length):
            #end of path
            if i ==-1:
                return -1
            
            #path previously seen
            if i in prev_seen:
                return -1
            
            #cycle detected
            if i in cur_seen:
                return length - cur_seen[i]+1
            
            cur_seen[i] = length+1
            
            return solution_1630_3_2(edges[i], length+1)
            
        
        res = -1
        prev_seen = {}
        for i in range(len(edges)):
            cur_seen={}
            length = solution_1630_3_2(i, 0)
            res = max(res, length)            
            prev_seen |= cur_seen

        return res