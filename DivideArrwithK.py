# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
# Return True if its possible otherwise return False.
# Example 1:
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.

def check_div_k(my_arr,k):
    x=len(my_arr)
    if x%k==0:
        print('True')
    else:
        print('False')

check_div_k([1,2,3,3,4,4,5,6],4)
check_div_k([1,2,3,4],3)