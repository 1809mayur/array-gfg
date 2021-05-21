
def get_sorted(arr,n):
    low = 0   # track for 0 position.
    mid = 0   
    high = n-1  # track the 2's position

    while mid <= high:    # mid should not be greater than high.

        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]   # swap 1 present at low position with the current mid.
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -= 1
        
    return arr 

def main():
    arr = list(map(int,input().split()))
    n = len(arr)
    res = get_sorted(arr,n)
    print(res)

if __name__ == "__main__":
    main()
            
