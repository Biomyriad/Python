
def i_sort(arr):
    for cur_elemt in range(0, len(arr)):
        idx = cur_elemt
        while arr[idx] < arr[idx-1] and idx > 0: # idx >= 0
            hldr = arr[idx-1]
            arr[idx - 1] = arr[idx]
            arr[idx] = hldr
            idx -= 1

arr = [6,5,3,1,8,7,2,4]
print(arr)
i_sort(arr)
print(arr)
