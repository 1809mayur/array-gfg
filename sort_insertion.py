def get_sorted(arr,n):
    sorted_arr = []   # assumed that this is sorted

    for i in range(n):
        pos = i 
        sorted_arr += [arr[i]]

        while pos > 0 and sorted_arr[pos] < sorted_arr[pos-1] :
            sorted_arr[pos], sorted_arr[pos-1] = sorted_arr[pos-1], sorted_arr[pos] 

            pos = pos - 1

    return sorted_arr

def main():
    arr = list(map(int,input().split()))
    n = len(arr)
    res = get_sorted(arr,n)
    print(res)

if __name__ == '__main__':
    main()
