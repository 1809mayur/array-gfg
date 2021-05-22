# Find one missing No. if it contains 1 to n-1 elements.Assume it have 1 to n numbers.

def get_missing_no(arr,n):  
    total = (n * (n+1)) // 2 

    total_of_array = sum(arr)

    return total - total_of_array

def main():
    arr = list(map(int,input().split()))
    n = int(input())  # last element that array can contain.

    res = get_missing_no(arr,n)
    print(res)

if __name__ == "__main__":
    main()