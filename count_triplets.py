
def countTriplets(arr, r):
    '''
    You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in geometric progression for a given common ratio r and i<j<k.
    
    For example, arr = [1,4,16,64]. If r = 4, we have [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3).
    
    Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given as an integer.
    
    countTriplets has the following parameter(s):
    
    arr: an array of integers
    r: an integer, the common ratio
    '''
    dic2 = {}
    dic3 = {}
    count = 0    
    for i in arr:
        
        if i in dic3:
            count += dic3[i]
                
        if i in dic2:
            if i*r in dic3:
                dic3[i*r] += dic2[i]
            else:
                dic3[i*r] = dic2[i]
        
        if i*r in dic2:
            dic2[i*r] += 1
        else:
            dic2[i*r] = 1
            
    return count        
