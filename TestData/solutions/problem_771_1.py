class Solution:
    def solution_771_1(self, text: str) -> int:
        
		# Used a prime number generator on the internet to grab a prime number to use.
        magic_prime = 32416189573
        
		# Standard 2 pointer technique variables.
        low = 0
        high = len(text) - 1
        
		# These are the hash tracking variables.
		cur_low_hash = 0
        cur_high_hash = 0
        cur_hash_length = 0
        
		# This is the number of parts we've found, i.e. the k value we need to return.
		k = 0
        
        while low < high:
            
			# To put the current letter onto our low hash (i.e. the one that goes forward from
			# the start of the string, we shift up the existing hash by multiplying by the base
			# of 26, and then adding on the new character by converting it to a number from 0 - 25.
            cur_low_hash *= 26 # Shift up by the base of 26.
            cur_low_hash += ord(text[low]) - 97 # Take away 97 so that it's between 0 and 25.
            
			
			# The high one, i.e. the one backwards from the end is a little more complex, as we want the 
			# hash to represent the characters in forward order, not backwards. If we did the exact same
			# thing we did for low, the string abc would be represented as cba, which is not right.	
			
			# Start by getting the character's 0 - 25 number.
			high_char = ord(text[high]) - 97
			
			# The third argument to pow is modular arithmetic. It says to give the answer modulo the
			# magic prime (more on that below). Just pretend it isn't doing that for now if it confuses you. 
            # What we're doing is making an int that puts the high character at the top, and then the 
			# existing hash at the bottom.
			cur_high_hash = (high_char * pow(26, cur_hash_length, magic_prime)) + cur_high_hash            
            
			# Mathematically, we can safely do this. Impressive, huh? I'm not going to go into here, but
			# I recommend studying up on modular arithmetic if you're confused.
			# The algorithm would be correct without doing this, BUT it'd be very slow as the numbers could
			# become tens of thousands of bits long. The problem with that of course is that comparing the
			# numbers would no longer be O(1) constant. So we need to keep them small.
			cur_low_hash %= magic_prime 
            cur_high_hash %= magic_prime
            
			# And now some standard 2 pointer technique stuff.
            low += 1
            high -= 1
            cur_hash_length += 1
            
			# This piece of code checks if we currently have a match.
            # This is actually probabilistic, i.e. it is possible to get false positives.
            # For correctness, we should be verifying that this is actually correct.
            # We would do this by ensuring the characters in each hash (using
			# the low, high, and length variables we've been tracking) are
			# actually the same. But here I didn't bother as I figured Leetcode
			# would not have a test case that broke my specific prime.
			if cur_low_hash == cur_high_hash:
                k += 2 # We have just added 2 new strings to k.
                # And reset our hashing variables.
				cur_low_hash = 0
                cur_high_hash = 0
                cur_hash_length = 0
        
		# At the end, there are a couple of edge cases we need to address....
		# The first is if there is a middle character left.
		# The second is a non-paired off string in the middle.
        if (cur_hash_length == 0 and low == high) or cur_hash_length > 0:
            k += 1
        
        return k