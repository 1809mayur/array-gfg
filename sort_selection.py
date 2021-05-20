def get_sorted(arr,n):
    # by selection sort.
    
    for start in range(n):
        pos = start
        
        for j in range(start,n):
            if arr[j] < arr[pos]:
                arr[j],arr[pos] = arr[pos],arr[j]
    return arr
    
def main():
    # arr = list(map(int,input().split()))
    arr =list(range(1000,-1,-1))
    n = len(arr)
    res = get_sorted(arr,n)
    print(res)
    
    
if __name__ == '__main__':
    main()