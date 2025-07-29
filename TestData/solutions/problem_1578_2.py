class Solution:
    def solution_1578_2(self, n: int, roads: List[List[int]]) -> int:
        
        '''The main idea is to count the frequency of the cities connected to roads and then 
           keep on assigning the integer value from one to n to each cities after sorting it. '''
        
        f = [0 for _ in range(n)]   # for storing the frequency of each city connected to pathways
        
        for x, y in roads:
            f[x] += 1
            f[y] += 1
        
        f.sort()
        s = 0
        for i in range(len(f)):
            s += f[i] * (i+1)  # assigning and storing the integer value to each cities frequency in ascending order
        return s