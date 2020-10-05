'''
Write a function return smallest element in the array
'''
import time
def my_fun(arr,n):
    t1=time.time()
    arr.sort()
    t2=time.time()
    print(t2-t1)   #Calculate Execution time
    return arr[0]

def mod_fun(arr,n):
    t1=time.time()
    my_min=10**9
    for i in arr:
        my_min=min(i,my_min)
    t2=time.time()
    print(t2-t1)
    return my_min


n=int(input())
arr=list(map(int,input().split()))
print(my_fun(arr,n))
print(mod_fun(arr,n))

'''
O/P==>
The tc==> O(nlog(n))  [Considering, python tim sort time complexity]
          For input of 10^6 it's showing TLE
Provided Brute_force method provide tc==>O(n)
           Working for 10^6 input array size comfortably.
'''
