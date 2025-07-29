class Solution:
    def solution_760_2(self, dominoes: List[List[int]]) -> int:
        
        #Keep track of the dominoes with a dictionary
		#counter[ DOMINO ] = COUNT
        counter = defaultdict( int );
        
        #Total will be the total number of pairs
        total = 0;
        
        #Go through all of the dominoes
        for i in range( len ( dominoes ) ):
            #Check the pair at the index
            pair = dominoes[ i ];
            
            #Pull the two values
            first = pair[ 0 ];
            second = pair[ 1 ];
            
            #Sort them by value
			#This way, the reversed matches will go into the same count
            smaller = min ( first, second );
            bigger = max( first, second );
            
            #Reassemble into tuple
			#This will act as our key for each domino
            pair_sorted = ( smaller, bigger );
            
            #If the current domino is already in our counter
            #Add to the total the previous matches
            
            #That is
            #If we have already added matching dominoes
            #Our current one will match with all the previous
            if pair_sorted in counter:
                total += counter[ pair_sorted ];
            
            #Lastly, we increment the count of the current
            counter [ pair_sorted ] += 1;
            
            
        return total;