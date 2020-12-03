
# Memoization 
def memo_subset_sum(boundary, running_sum):
    

    # If previously computed, return the count of valid combinations
    if (boundary, running_sum) in memo:
        return memo[(boundary, running_sum)]
    
    # Otherwise compute it and add to the dictionary 
    valid_count = subset_sum(boundary, running_sum)
    memo[(boundary, running_sum)] = valid_count
    return valid_count


# Approaching the staircase problem as a subset sum
def subset_sum(boundary, running_sum = 0):
    
    # If target reached, indicate a valid combination reached by adding 1 to 'valid_count'
    if running_sum == target: 
        return 1
      
    # If beyond target, stop      
    if running_sum > target:
        return 0  
    
    valid_count=0
    
    
    # If target has not been reached and options remain, explore them by looking at subsequent boundaries
    
    remaining=target-boundary
    
    if remaining==0:
        return valid_count
    
    
    for i in range(remaining):
        n = boundary
        remaining_options = boundary+1
        
        valid_count+=memo_subset_sum(remaining_options, running_sum + n) 
        boundary+=1
    
    return valid_count
   
    
    
def solution(n):
    
    global target
    global memo
    
    # Initialize a dict for memoization
    memo={}

    target=n
    
    # The smallest number that the combination being explored can start with 
    # Initialized
    boundary=1
    
    return(subset_sum(boundary))

    


