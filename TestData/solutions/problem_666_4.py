class Solution:
    def solution_666_4(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        first_list_pointer = 0
        
        second_list_pointer = 0
        
        ans = []
        
        while first_list_pointer < len(firstList) and second_list_pointer < len(secondList):
            
            # find if the two intervals are overlaping, two intervals are said to overlap
            # if max(start1, start) <= min(end1, end2)
            
            max_start = max(firstList[first_list_pointer][0], secondList[second_list_pointer][0])
            min_end = min(firstList[first_list_pointer][1], secondList[second_list_pointer][1])
            
			# Intersecting condition
            if max_start <= min_end:
                ans.append([max_start, min_end])
            
            # search for next higher end time for interval in either firstList or secondlist
            if firstList[first_list_pointer][1] > secondList[second_list_pointer][1]:
                second_list_pointer += 1
            else:
                first_list_pointer += 1
        
        return ans
                
Second Aproach

class Solution:
    def solution_666_4(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        p1 = p2 = 0
        while p1 < len(firstList) and p2 < len(secondList):
            aux = [firstList[p1], secondList[p2]]
            aux.sort()
            if aux[0][0] <= aux[1][0] <= aux[0][1]:
                ans.append([max(firstList[p1][0], secondList[p2][0]),min(firstList[p1][1], secondList[p2][1])])
            if firstList[p1][1] <= secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return ans