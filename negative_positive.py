# In this problem we will separate the array into into region of negative and positive.

def negative_positive_separator(arr,n):
    low = 0   # requirement for negative integer at this low position.
    i = 0    # iterator

    while i < n:

        if arr[i] < 0 :
            arr[low],arr[i] = arr[i],arr[low]
            i += 1
            low += 1
        else:
            i += 1

    return arr     # O(n) complexity and constant space.


def main():
    arr = list(map(int,input().split()))
    n = len(arr)

    res = negative_positive_separator(arr,n)
    print(res)

if __name__ == "__main__":
    main()

