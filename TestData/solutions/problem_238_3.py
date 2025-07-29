class Solution:
    #Let n = len(intervals)!
    #Time-Complexity: O(n + nlogn + n*log(n)) -> O(nlogn)
    #Space-Complexity: O(n + n) -> O(n)
    def solution_238_3(self, intervals: List[List[int]]) -> List[int]:
        
        #Brute-Force Approach: For every interval, linearly consider every other intervals
        #and constantly update the lowest start value s.t. it is >= current interval's
        #end value! 
        ans = []
        hashmap = {}
        arr_of_starts = []
        #initializing hashmap by mapping keys as start values to the index pos. of the interval it
        #belongs within!
        for i in range(len(intervals)):
            if(intervals[i][0] not in hashmap):
                hashmap[intervals[i][0]] = i
                arr_of_starts.append(intervals[i][0])
                continue
                
        #need to sort the arr_of_starts beforehand!
        arr_of_starts.sort()
        
        #iterate for each interval from left to right and find the interval with start value that's minimal
        #s.t. it's greater than or equal to current interval's end value!
        for j in range(len(intervals)):
            cur_end = intervals[j][1]
            #first, check if right interval is of itself!
            if(cur_end == intervals[j][0]):
                ans.append(j)
                continue
            #define search space w/ respect to arr of starts!
            L, R = 0, len(arr_of_starts) - 1
            index, lowest_start = -1, float(inf)
            #as long as binary search has at least one element, continue iterations of bin. search!
            while L <= R:
                mid = (L + R) // 2
                mid_e = arr_of_starts[mid]
                
                #check if current middle candidate start value is >= cur_end!
                if(mid_e >= cur_end):
                    #check if current candidate start value beats the lowest_start!
                    if(mid_e < lowest_start):
                        lowest_start = mid_e
                        index = hashmap[lowest_start]
                        #there might be even smaller values of start that satisfies criteria!
                    R = mid - 1
                    continue
                        
                #if current start value is too small, we need to search towards right portion!
                else:
                    L = mid + 1
                    continue
            ans.append(index)
        return ans