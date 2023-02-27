def miniMaxSum(arr):
    
    # Sorting the array
    sorted_array = arr.sort()

    min_sum = sum(arr[0:4])
    max_sum = sum(arr[1:5])
    
    print(min_sum, max_sum)

# Sample Input

arr = [1,3,5,7,9]

miniMaxSum(arr)