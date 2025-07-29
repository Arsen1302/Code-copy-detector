class Solution:
    def solution_731_5(self, barcodes: List[int]) -> List[int]:
        # Get the counts of all of our barcode elements.
        cnts = collections.Counter(barcodes)
		# Put the -'ve counts along with themselves into a min heap.
		# For those new to this we use -'ve because this is a min heap, so largest cnt pop'd first.
        heap = [(-v, k) for k,v in cnts.items()]
        heapq.heapify(heap)
        res = []
        # While we have elements on our heap.
        while heap:
		    # pop the top element.
            cnt1, num1 = heapq.heappop(heap)
			# If the top element was the last we used, we need something different.
            if res and res[-1] == num1:
			    # pop the next highest cnt element. 
                cnt, num = heapq.heappop(heap)
                res.append(num)
                cnt += 1
				# If there's still elements left we put them back on the heap.
                if cnt != 0:
                    heapq.heappush(heap, (cnt, num))
				# We can also add the first that we popped, and push it back on the heap as well.
                res.append(num1)
                cnt1 += 1
                if cnt1 != 0:
                    heapq.heappush(heap, (cnt1, num1))
			# else we just add the highest cnt element and put the remaining back on.
            else:
                res.append(num1)
                cnt1 += 1
                if cnt1 != 0:
                    heapq.heappush(heap, (cnt1, num1))
            
        return res