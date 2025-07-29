class Solution:
    #Let n = len(queries) and m = len(words)
    #Time-Complexity: O(m + mlog(m) + n*log(m)) -> O(mlog(m) + nlog(m))
    #Space-Complexity: O(10*m + n*10 + m) -> O(n + m)
    def solution_780_4_1(self, queries: List[str], words: List[str]) -> List[int]:
        
        #Approach: Traverse linearly through each and every word in words array
        #and get its function value and append it to seperate array!
        #Then, sort the separate array in increasing order.
        #Then, for each ith query, get the function value from applying
        #function on ith query string -> look for leftmost index in
        #new array s.t. from that particular index onwards, all values
        #will be larger than the ith query function value!
        
        #This will help us get number of words in words input array that
        #have higher function value than current query!
        
        #We need to also define solution_780_4_2 function that computes
        #function value for any non-empty string!
        def solution_780_4_2(s):
            hashmap = {}
            for c in s:
                if c not in hashmap:
                    hashmap[c] = 1
                    continue
                else:
                    hashmap[c] += 1
            #iterate through each key value and put it in array of tuples,
            #where first element is letter and second element is its frequency!
            
            array = []
            for k,v in hashmap.items():
                array.append((k, v))
            #then sort the array by lexicographical order: first element of tuple!
            array.sort(key = lambda x: x[0])
            #return the first element of array: lexicographically smallest
            #char frequency!
            return array[0][1]
        ans = []
        arr = []
        for word in words:
            arr.append(solution_780_4_2(word))
        #sort the new array arr!
        arr.sort()
        
        #iterate through each and every query!
        for query in queries:
            requirement = solution_780_4_2(query)
            #initiate binary search to find leftmost index pos in arr!
            l, r = 0, (len(arr) - 1)
            leftmost_index = None
            while l <= r:
                mid = (l + r) // 2
                middle = arr[mid]
                if(middle > requirement):
                    leftmost_index = mid
                    r = mid - 1
                    continue
                else:
                    l = mid + 1 
                    continue
            #once binary search is over, we should have leftmost index!
            #Append the difference val since it tells number of words
            #with function value greater than requirement!
            
            #we have to check whether leftmost_index still equals None ->
            #if none of words in words array have function val greater than
            #the requirement!
            if(leftmost_index == None):
                ans.append(0)
                continue
            ans.append(len(arr) - leftmost_index)
        return ans