'''
author: Diksha Verma
date: 04-10-20 09:19 
title : Kadane's Algorithm in Python, Also known as Largest Sum Contiguous Subarray
Time Complexity: O(n)
'''
# Function to find the maximum contiguous subarray 
def Kadane(array,size):
    current_sum = 0
    best_sum = 0 
    for i in range(size):
        current_sum += array[i]
        if best_sum < current_sum:
            best_sum = current_sum 
        if current_sum < 0:
            current_sum = 0 
    return best_sum 
    
    
def main():
    # input_list = list(map(int,input().split()))
    input_list = [-2, -3, 4, -1, -2, 1, 5, -3]  
    size_list = len(input_list)
    print(Kadane(input_list,size_list))
    
main()
