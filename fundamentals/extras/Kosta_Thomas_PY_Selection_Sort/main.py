def s_sort(arr):
    for i in range(0, len(arr) - 1):
        lowest_val = i
        for x in range(i+1,len(arr)):
            if arr[x] < arr[lowest_val]:
                lowest_val = x
        if not lowest_val == i:
            hldr = arr[i]
            arr[i] = arr[lowest_val]
            arr[lowest_val] = hldr

arr = [8,5,2,6,9,3,1,4,0,7]

print(arr)
s_sort(arr)
print(arr)