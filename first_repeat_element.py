# Here we will find the first repeated element in an array.


def get_first_repeat(arr,n):

    hashmap = dict()
    for i in range(n):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = 1
        else:
            hashmap[arr[i]] += 1
    
    for i in arr:
        if i in hashmap:
            if hashmap[i] > 1:
                return i
    return -1

arr = [10,5,3,4,3,5,6]
n = len(arr)
print(get_first_repeat(arr,n))