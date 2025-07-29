class Solution(object):
    def solution_638_2_1(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def solution_638_2_2(state):
            return tuple([1 if i>0 and i<len(state)-1 and state[i-1] == state[i+1] else 0 for i in range(len(state))])
        
        seen = {}
        state = tuple(cells)
        i = 0
        remaining = 0
        while i < N:
            if state in seen:
                cycle = i - seen[state]
                remaining = (N-i)%cycle
                break
            seen[state] = i
            state = solution_638_2_2(state)
            i+=1
        
        while remaining > 0:
            state = solution_638_2_2(state)
            remaining-=1
        return state