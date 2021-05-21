
def main():
    arr = list(map(int,input().split()))  # input for an array.
    n = len(arr)
    
    maxi = max(arr)  # maximum of an array.
    mini = min(arr)  # minimum of an array.

    Range = maxi - mini  # here we get range.

    cofficient = Range / (maxi+mini)

    print("Range is : ",Range)
    return("Coefficient of Range is: " + str(cofficient))

print(main())