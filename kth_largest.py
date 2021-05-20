
def get_first_k_largest(arr,n,k):
    
    arr.sort(reverse=True)
    return arr[:k]

def main():
    arr = list(map(int,input().split()))
    n = len(arr)
    k = int(input())  # first k largest elements k < n.

    res = get_first_k_largest(arr,n,k)
    print(res)

    for i in res:
        print(i,end=" ")


if __name__ == '__main__':
    main()
