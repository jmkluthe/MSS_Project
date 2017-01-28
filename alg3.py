#!/usr/bin/python

def divcon(A, first, last):#note: the 'last' element is not checked
    #base case: no elements
    if last == first:
        return (0, 0, 0)
    #base case: 1 elements            
    elif first == last-1:
        if A[first] > 0:
            return (A[first], first, last)
        else:
            return (0, first, first)

    else:
        middle = (first + last) // 2 #divide
        #get the maximum sum from 0 to middle
        sum = 0
        indexleft = middle #index of where the greatest subarray 'ends'
        maxleft = 0  #stores the greatest sum up til that point
        for n in range(middle-1, first-1, -1):
            sum += A[n]
            if sum > maxleft:
                maxleft = sum
                indexleft = n
                
        #get the maximum sum from middle to the end
        sum = 0 #reset the sum
        indexright = middle #index of where the greatest subarray 'ends'
        maxright = 0 #stores the greatest sum up til that point
        for i in range(middle+1, last+1, +1):
            sum += A[i-1]
            if sum > maxright:
                maxright = sum
                indexright = i

        #take the overlap of the two max subarrays on each side
        overlap = (maxleft+maxright, indexleft, indexright)
        #find the max subarray out of the left, right, and 'middle' sections
        maxsub = max(divcon(A, first, middle), divcon(A, middle, last), overlap)
        return maxsub

def alg3(A):#helper function
    result = divcon(A, 0, len(A))
    return(A[result[1]:result[2]], result[0])


#myArray=[31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
#
#print alg3(myArray)
