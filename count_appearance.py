
def get_total_apperance(arr,num):
    count = 0
    for i in arr:  # iterating over each element in array.
        if i == num :  # checking if that number equal to the input number.
            count += 1
    
    return count  # O(n) complexity with constanct space complexity.

def main():
    arr = list(map(int,input().split()))
    num = int(input())
    result = get_total_apperance(arr,num)
    print(result)


if __name__ == '__main__':
    main()