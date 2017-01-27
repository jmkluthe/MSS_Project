#!/usr/bin/python3

"""
This algorithm relies on the fact that for each subarray ar A[0 ... n - 1] that has the
form S[0 ... j + 1], where j + 1 <= n - 1, there are three possible locations for a
subsubarray with a maximum sum: First, it could be a previously found maximum value
within S[0 ... j]; Second, it could be S[j + 1]; Third, it could be S[j + 1} plus the
largest sum found so far that ends at index j.

Therefore, we keep track of max for the true maximum sum subarray found so far, max_to_j
for the current maximum subarray ending at j, and the index values for the beginning and
end of max, and the beginning of max_to_j. If S[j + 1] is bigger than itself plus max_to_j,
then it replaces the value of max_to_j. Otherwise, it is added onto max_to_j, creating
the next largest sum ending at j for the next iteration. Then, if max_to_j, which now
either equals S[j + 1] or equals the maximum known sum ending at j plus S[j + 1], is
larger than the current max, we replace the value of max with it, and the values of the
starting and ending indexes for max with the appropriate values.
"""

def linear_max_subarray(arry):
    max = max_to_j = arry[0]
    beg_max = end_max = beg_mtj = 0
    for j in range(1, len(arry)):
        jp1 = arry[j]
        if jp1 > max_to_j + jp1:
            max_to_j = jp1
            beg_mtj = j
        else:
            max_to_j += jp1
        if max_to_j > max:
            max = max_to_j
            beg_max = beg_mtj
            end_max = j
    return arry[beg_max:end_max+1], max

