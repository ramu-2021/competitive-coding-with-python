'''
Write a function return smallest element in the array
'''
def my_fun(arr,n):
    arr.sort()
    return arr[0]
n=int(input())
arr=list(map(int,input().split()))
print(my_fun(arr,n))
