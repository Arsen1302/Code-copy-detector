class Solution:
    def solution_741_3(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:

        # collect the highest values for each label
        highest = collections.defaultdict(list)

        # find the highest values
        for label, value in zip(labels, values):
            if len(highest[label]) < useLimit:
                heapq.heappush(highest[label], value)
            else:
                heapq.heappushpop(highest[label], value)

        
        # get the resulting values
        values = []
        for vals in highest.values():
            values.extend([-val for val in vals])

        # check whether we can use all
        if len(values) <= numWanted:
            return -sum(values)
        
        # heapify the values
        heapq.heapify(values)

        # make the sum
        result = 0
        for _ in range(numWanted):
            result += heapq.heappop(values)
        
        return -result