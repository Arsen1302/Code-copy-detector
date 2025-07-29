class Solution:
    def solution_363_4(self, n: int, k: int) -> int:
        # set dynamically programmed values array original 
        # this is where we will store the final nth run of the algorithm 
        # we will also store the prior nth valuation here up until the end 
        dynamically_programmed_values = [0]*(k+1)
        # set the modulo_values as the value to take the modulo of when needed 
        modulo_values = int(1e9 + 7) 
        # set n_index at starting value of 1 
        # loop over range of n values 
        for n_index in range(1, n+1) :
            # build and set a temp dynamically programmed values for this nth index  
            # this becomes the current row which we are building using the prior row which we have already built 
            temp_dynamically_programmed_values = [0]*(k+1)
            temp_dynamically_programmed_values[0] = 1
            # set k_index at starting value of 1 
            # loop over range of k values 
            for k_index in range(1, k+1) :
                # get original value result as the value at the index already listed + modulo_values  
                value = (dynamically_programmed_values[k_index] + modulo_values)
                # if we are at a k_index greater than the n_index 
                if k_index >= n_index : 
                    # reduce the value by the prior value, otherwise, by 0 
                    value -= dynamically_programmed_values[k_index - n_index]
                # modulo the current value 
                value %= modulo_values
                # get the prior value, add to it the current value, and modulo
                prior_value = temp_dynamically_programmed_values[k_index - 1] 
                current_value = value + prior_value 
                current_value %= modulo_values
                # set the temporary dynamically programmed values at k_index to the current value 
                temp_dynamically_programmed_values[k_index] = current_value
            # update the final dynamically programmed values listing (aka, set the new prior row)
            dynamically_programmed_values = temp_dynamically_programmed_values
            
        # if k is greater than zero, get the prior_value (one before the kth instance)
        if k > 0 : 
            prior_value = dynamically_programmed_values[k-1]
        else : 
            prior_value = 0
        # final value is the final kth instance plus the modulo values 
        final_value = dynamically_programmed_values[k] + modulo_values
        # return is the difference of the kth and penultimate value, modulo by modulo values 
        return_value = (final_value - prior_value) % modulo_values
        # int cast on return 
        return int(return_value)