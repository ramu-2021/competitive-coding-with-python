'''
Write a function return smallest element in the array
'''
def my_fun(arr,n):
    my_min=10**9
    for i in arr:
        my_min=min(i,my_min)
    return my_min
n=int(input())
arr=list(map(int,input().split()))
print(my_fun(arr,n))
