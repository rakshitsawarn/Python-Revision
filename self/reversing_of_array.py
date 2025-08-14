def reversing_of_an_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end]  = arr[end], arr[start]
        start+=1
        end-=1
    return arr
print(reversing_of_an_array([1, 2, 3, 4, 5]))