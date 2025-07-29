class Solution:
    def solution_369_5_1(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        #Approach: At every decision making node, we have an option to choose one of 
        #many available sale special offers! Once we run out of offers to choose from,
        #we will simply have to buy the remaining items needed at regular price described
        #from price array!
        
        #To keep track of the special offer I used so far, I will utilize a boolean array
        #s.t. b_arr[i] = 1 if already used 0 else!
        num_specials = len(special)
        b_arr = [0 for _ in range(num_specials)]
        
        #i will also use nonlocal variable to keep track of amount spent so far!
        #i will periodically update this as I recurse and also when I backtrack!
        amount_spent = 0
        #n will store the original number of items I need to buy!
        n = sum(needs)
        ans = float(inf)
        #paramter:
        #1. rem. total elements to buy!
        #2. array describing number of rem. items by item type!
        def solution_369_5_2(remaining, a):
            nonlocal b_arr, num_specials, amount_spent, ans, special, price
            #base case: rem. items == 0! We reach this base case if we are able to buy
            #every item type according to our needs just from using special offers and not 
            #paying at regular price!
            if(remaining == 0):
                #update answer!
                ans = min(amount_spent, ans)
                return
            
            #if not base case, that means we still have items to buy!
            #consider iterating through each and every special offer! 
            #check that it's available!
            #if available, check that speical offer does not require buying items more than need!
            #If so, deduct amount of items by each item type and update remaining amount
            #and recurse on it!
            #When recursing, restore state of b_arr, amount_spent, as well as array a!
            special_valid = False
            for i in range(num_specials):
                #ith offer already used!
                if(b_arr[i] == 1):
                    continue
                #run a loop to check if ith offer amount to buy never exceeds the
                #current needs!
                is_valid = True
                for j in range(len(a)):
                    #check if ith special offer causes overbuying! If so, set is_valid flag off!
                    if(a[j] < special[i][j]):
                        is_valid = False
                        break
                #check if flag is not set!
                if(not is_valid):
                    continue
                special_valid = True
                #otherwise, if current ith special offer is valid for all item types,
                #go ahead and update remaining items, state of array a, as well as amount spent!
                amount_spent += special[i][-1]
                
                #set the boolean array on to indicate we used up ith offer!
                b_arr[i] = 1
                overall_remaining = remaining
                for b in range(len(a)):
                    a[b] -= special[i][b]
                    overall_remaining -= special[i][b]
                
                #go ahead and recurse!
                solution_369_5_2(overall_remaining, a)
                
                #once we return from rec. call, set the flag back off,
                #update amount spent, as well as state of array a when
                #backtracking to parent caller in recursion!
                b_arr[i] = 0
                #update amount spent!
                amount_spent -= special[i][-1]
                
                for c in range(len(a)):
                    a[c] += special[i][c]
            #check if even a single special offer can be used by using special_valid boolean flag!
            #If not, then we have to buy remaining items and update amount_paid so far! 
            if(not special_valid):
                new_amount_paid = amount_spent
                for d in range(len(a)):
                    if(a[d] > 0):
                        new_amount_paid += (a[d] * price[d])
                ans = min(ans, new_amount_paid)
                        
        
        solution_369_5_2(n, needs)
        #edge case: without using any special offer, buying at regular price might be the best
        #option!
        without = 0
        for z in range(len(price)):
            without += (price[z] * needs[z])
        return min(ans, without)