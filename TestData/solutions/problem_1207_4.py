class Solution:
    def solution_1207_4(self, nums1: List[int], nums2: List[int]) -> int:
        # make sure nums1 has the larger sum
        highSum, lowSum = sum(nums1), sum(nums2)
        if highSum == lowSum:
            return 0
        if highSum < lowSum:
            nums1, nums2 = nums2, nums1
            highSum, lowSum = lowSum, highSum

        # push nums1 into max heap
        # push nums2 into min heap
        maxHeap = []
        for num in nums1:
            heapq.heappush(maxHeap, -num)
        minHeap = []
        for num in nums2:
            heapq.heappush(minHeap, num)

        count = 0
        while highSum != lowSum:
            count += 1
            diff = highSum - lowSum
            high = -maxHeap[0]
            low = minHeap[0]
            # pick the biggest change
            hightDelta = high - 1
            lowDelta = 6 - low
            # end case -- impossible
            if hightDelta == lowDelta == 0:
                return -1
            if hightDelta >= lowDelta:
                if hightDelta >= diff:
                    break
                else:
                    # update sum and heap after change
                    heapq.heapreplace(maxHeap, -1)
                    highSum -= hightDelta
            else:
                if lowDelta >= diff:
                    break
                else:
                    # update sum and heap after change
                    heapq.heapreplace(minHeap, 6)
                    lowSum += lowDelta

        return count