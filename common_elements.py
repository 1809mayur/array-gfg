

def common_elements(v1,v2):
    # we assumed that v1.length > v2.length

    # if by chance v2.length > v1.length then we will exchange them.
    if len(v2)>len(v1): 
        v2,v1 = v1,v2

    # We are solving it with hashmap.
    hashmap = dict()

    # iterate over array whose length is max and store its element as key and counting of occurence as a value.
    for i in range(len(v1)):
        if v1[i] not in hashmap:
            hashmap[v1[i]] = 1
        else:
            hashmap[v1[i]] += 1
    
    #  Now here we check the common between two arrays.
    ans = []
    for i in v2:
        if i in hashmap:
            if hashmap[i] > 0 :
                hashmap[i] -= 1
                ans.append(i)
                
    
    return ans

def main():
    # Consider v1 length is greater than v2 length.
    v1 = list(map(int,input().strip().split()))
    v2 = list(map(int,input().strip().split()))

    res = common_elements(v1,v2)
    print(res)


if __name__ == "__main__":
    main()


