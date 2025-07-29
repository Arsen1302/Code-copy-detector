class Solution:
    def solution_1260_3(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
		# To store the output result
        lis = [0 for i in range(len(queries))]
		#sort the intervals in the reverse order
        intervals.sort(reverse = True)
		#View the intervals list
        print(intervals)
		#store the index number of the query with query number
        queriesWithIndex = sorted([(q,i) for i,q in enumerate(queries)])
		#Print and view the queriesWithInd
        print(queriesWithInd)
		#decare the lis to store the valuew but with the help of heap so the it will be store in sorted form
        heapLis = []
		#Traverse the queryWithIndex list which consists of tuples
        for query,i  in queriesWithIndex:
			# loop should run till the intervals becomes empty
            while len(intervals)  and query >=intervals[-1][0]:
				#pop the last value from interval and store it in start and end value
                start, end = intervals.pop()
				#push the value in the heap list
                heappush(heapLis,[end - start + 1, end])
			# traverse till the heaplis becomes empty or the element in heapLis[0][1] < query
            while len(heapLis) and heapLis[0][1] < query:
                #pop the tuple from the heapLis
				heappop(heapLis)
			#if len(heapLis) is 0 then simply assign lis to -1 else assign the value of heapLis[0][0] to lis[i]
            if len(heapLis) == 0:
                lis[i] = -1
            else:
                lis[i] = heapLis[0][0]
		#return the lis
        return lis