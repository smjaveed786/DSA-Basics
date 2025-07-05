#Binary search
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1

size=int(input("Enter the size of array :"))
arr=[]
print("Enter the elements")
for i in range(size):
    num=int(input(f"Element {i+1} :"))
    arr.append(num)
key=int(input("Enter the element to search :"))
result = binary_search(arr,key)
if result != -1:
    print(f"\n Element {key} found at {result}")
else:
    print(f"\n Element {key} not found" )