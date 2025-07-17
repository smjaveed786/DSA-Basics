#Insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
size=int(input("enter the no.of elements :"))
arr=[]
print("Enter ",size,"elements")
for _ in range(size):
    num=int(input())
    arr.append(num)
result= insertion_sort(arr)
print("Sorted array :", result)
