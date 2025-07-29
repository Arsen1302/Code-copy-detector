class Solution:
    def solution_631_5(self, deck: List[int]) -> List[int]:
        deck.sort()                                     # You can sort in ascending or descending if you are using for loop but if using pop() method, only sort in ascending.
        q = deque([deck[-1]])                    # Initialised deque object with the max deck value. 
                                                     # Remember you can always just use pop() function on the deck list. I just chose not to.
        for i in range(len(deck)-2 ,-1 ,-1):         # Use while deck here if you are going for the pop() approach 
            q.appendleft(q.pop())                    # Bringing the last element in the queue to the front 
            q.appendleft(deck[i])                    # Adding the next largest element from deck to the front of our queue
            
        return list(q)                               # You can just return q, it would still be correct.