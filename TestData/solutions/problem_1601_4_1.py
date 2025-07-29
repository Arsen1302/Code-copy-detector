class Solution:
    def solution_1601_4_1(self, n: int) -> int:
        
        
        edgeList = {
            1: [2,3,4,5,6],
            2:[1,3, 5],
            3:[1, 2, 5, 4],
            4:[1, 3, 5],
            5:[1,2,3,4,6],
            6:[1, 5]
        }
        
        dp = dict()
        
        def solution_1601_4_2(curr_node, prev_node, sequence_length):
            
            if sequence_length == 1:
                return 1
            if (curr_node, prev_node, sequence_length) in dp:
                return dp[(curr_node, prev_node, sequence_length)]
            count = 0
            for node in edgeList[curr_node]:
                if node != prev_node:
                    count += solution_1601_4_2(node, curr_node, sequence_length-1)
            dp[(curr_node, prev_node, sequence_length)] =count
            return count
        ans = 0
        for i in range(1, 7):
            ans += solution_1601_4_2(i, -1, n)
            ans = ans % int(1e9+7)
        return ans