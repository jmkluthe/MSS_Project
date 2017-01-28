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
        maxleft = (0, middle)   #stores the greatest sum up til that point, and the position where that subarray 'ends' on the left
        for i in range(middle-1, first-1, -1):
            sum += A[i]
            if sum > maxleft[0]:
                maxleft = (sum,i)
                
        #get the maximum sum from middle to the end
        sum = 0
        maxright = (0, middle) #stores the greatest sum up til that point, and the position where that subarray 'ends' on the right
        for j in range(middle+1, last+1, +1):
            sum += A[j-1]
            if sum > maxright[0]:
                maxright = (sum,j)

        overlap = (maxleft[0]+maxright[0], maxleft[1], maxright[1])

        return max(divcon(A, first, middle),
                   divcon(A, middle, last),
                   overlap)
def alg3(A):#helper function
    result = divcon(A, 0, len(A))
    return(A[result[1]:result[2]], result[0])


# myArray=[31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
#
# print alg3(myArray)