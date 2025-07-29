class Solution:
    def solution_1451_5(self, left: int, right: int) -> str:
        ans = 1                                                                  //Initialise the product with 1
        while left <= right:                                               // Start the multiplying numbers in
            if left == right:                                                 // Exception case when left is right else the number will be multiplied 2 times
                ans *= left                                                   //then only multiply either left or right
            else:
                ans *= left * right                                        // Else multiply left and right numbers and multiply with ans
            left += 1                                                         // Increment left by one
            right -= 1                                                        //Decrement right by 1
        count = 0                                                           // Initialise count of trailing zeroes
        ans = str(ans)                                                    // Converting integer to string
        i = len(ans) - 1                                                  // Start the pointer with end of string
        while i >= 0 and ans[i] == '0':                          // Decrement pointer by one while the value at pointer is 0
            count += 1                                                   //and increase the count of trailing zeroes
            i -= 1
        fans = ''                                                            //Empty string which will store the number without the trailing zeroes
        for j in range(i+1):                                            // will use the i pointer which stored the last location of the trailing zero
            fans += ans[j]                                              //store each character until the trailing zero isn't reached
        final = ''                                                           //Final ans which will give the required result 
        if len(fans) > 10:                                              //If the length of the number without the trailing zeroes has a length greater than 10
            temp1 = ''                                                   //Will store the first 5 character of the number
            for j in range(5):                                          // Adding the first 5 characters
                temp1 += fans[j]
            temp2 = ''                                                   //Will store the last 5 characters of the number
            for j in range(-5,0):                                      // Add the last 5 characters
                temp2 += fans[j]
            final = temp1 + '...' + temp2 + 'e' + str(count)           //Final ans with first 5 character, last 5 characters + e + count of trailing zeroes
        else:                                                                    //If length of the number is less than 10
            final = fans + 'e' + str(count)                         // Final ans with number without trailing zeroes + e + count of trailing zeroes
        return final                                                      //Return the final string