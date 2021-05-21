# Here we will rotate the array in cyclic order upto one place.
# [1,2,3,4,5]  == [5,1,2,3,4]

def cyclic_rotate(arr,n):

    last_element = arr.pop()
    arr.insert(0,last_element)
    return arr 

def main():
    arr = list(map(int,input().split()))
    n = len(arr)

    res = cyclic_rotate(arr,n)
    print(arr)

if __name__ == "__main__":
    main()