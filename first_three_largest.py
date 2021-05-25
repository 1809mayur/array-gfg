# Here we will find the first three largest elements.

# O(NlogN) AND O(1) space.
def get_by_sorting(arr,n):
    arr.sort(reverse = True)

    count = 0
    ans = []
    for i in arr:
        if count < 3:
            ans.append(i)
            count += 1
    return ans   


# It take O(n) complexity but space complexity is high. 
def get_by_extra_space_of_list(arr,n):
    maxi = max(arr)

    ls = [0] *(maxi+1)

    for i in arr:
        ls[i] = 1
    
    count = 0
    ans = []
    for i in range(maxi,-1,-1):
        if count < 3:
            if ls[i]:
                ans.append(i)
                count += 1
    return ans


arr = [10,4,3,50,23,90]
n = len(arr)
print(get_by_extra_space_of_list(arr,n))
print(get_by_sorting(arr,n))
            
            