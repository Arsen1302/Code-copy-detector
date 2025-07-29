class Solution:
    def solution_774_1_1(self, text: str) -> int:
        first_occurence,last_occurence = {},{}
        ans,prev,count = 1,0,0
        n = len(text)
        
        for i in range(n):
            if text[i] not in first_occurence: first_occurence[text[i]] = i
            last_occurence[text[i]] = i
            
        for i in range(n+1):
            if i < n and text[i] == text[prev]:
                count += 1
            else:
                if first_occurence[text[prev]] < prev or last_occurence[text[prev]] > i : count += 1
                ans = max(ans,count)
                count = 1
                prev = i
        
        def solution_774_1_2(item,before,after):
            count = 0
            while before >= 0 and text[before] == item: 
                count += 1
                before -= 1
            while after < n and text[after] == item:
                count += 1
                after += 1
            if first_occurence[item] <= before or last_occurence[item] >= after:count+=1
            return count
        
        for i in range(1,n-1):
            ans = max(ans,solution_774_1_2(text[i+1],i-1,i+1))
        return ans