#You are given an array of integers (both positive and negative). Find the continuous
#Sequence with the largest sum. Return the sum.  
#EXAMPLE
#Input: {2, -8, 3, -2, 4, -10}
#Output: 5 (i.e., {3, -2, 4} )



from sys import maxsize

def maxSubArraySum(a,size): 
  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i] 
  
        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
  
    print ("Maximum contiguous sum is %d"%(max_so_far)) 
    print ("Starting Index %d"%(start)) 
    print ("Ending Index %d"%(end))
    print(a[start:end+1])


a=[2,-8,3,-2,4,-10]
b=maxSubArraySum(a,5)
print(b)
 
