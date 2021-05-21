
def merge(a1,a2,m,n):
    i,j = 0,0
    a3 = []   # contains union of both array in sorted order.
    a4 = []   # contains intersection of both array.
    while (i+j) < (m+n)-1:
        if i >= m:
            a3 += a2[j:]
            break
        if j >= n:
            a3 += a1[i:]
            break

        if a1[i] < a2[j]:
            a3.append(a1[i])
            i += 1
        elif a2[j] < a1[i] :
            a3.append(a2[j])
            j += 1
        else:
            a4.append(a1[i])
            a3.append(a1[i])
            i += 1
            j += 1
    print("Intersection of a1 and a2 : {}".format(a4))
    return "Union of a1 and a2 :" , a3



def  main():
    a1 = list(map(int,input().split()))
    m = len(a1)
    a2 = list(map(int,input().split()))  
    n = len(a2)

    res = merge(a1,a2,m,n)
    print(res)


if __name__ == "__main__":
    main()