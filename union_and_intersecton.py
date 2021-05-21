# Here we will do union and intersection bth list but by using an set.


def union_and_intersection(a1,m,a2,n):
    # both concetanated into a1.
    a1 += a2   

    # Now our task is to remove duplicates.
    union_of_both = set(a1) 

    hashmap = dict()
    for i in a1:          # here we will get a hashmap which contain a number as a key and total occurence as a value.
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    # Now our task is to get number whose occurence is more than 1.
    intersection_ls = []
    for i in hashmap:
        if hashmap[i] > 1:
            intersection_ls += [i]

    print("Union Of Both Array: ",list(union_of_both))
    return "Intersection Of Both: ",intersection_ls

def main():
    a1 = list(map(int,input().split()))
    m = len(a1)
    a2 = list(map(int,input().split()))
    n = len(a2)

    res = union_and_intersection(a1,m,a2,n)
    print(res)

if __name__ == "__main__":
    main()