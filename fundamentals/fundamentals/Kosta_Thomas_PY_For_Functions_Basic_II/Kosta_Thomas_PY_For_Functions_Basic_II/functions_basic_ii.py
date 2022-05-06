
# Countdown 
def countdown(startInt):
    result = []
    for i in range(startInt,0-1,-1):
        result.append(i)
    return result

print(countdown(5))

# Print and Return
def print_and_return(arr):
    print(arr[0])
    return arr[1]

print(print_and_return([1,2]))

# First Plus Length
def first_plus_length(arr):
    return arr[0] + len(arr)

print(first_plus_length([1,2,3,4,5]))

# Values Greater than Second
def values_greater_than_second(arr):
    if len(arr) < 2: return False
    secondVal = arr[1]
    result = []
    for i in range(0,len(arr)):
        if arr[i] > secondVal:
            result.append(arr[i])
    print(len(result))
    return result

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# This Length, That Value 
def length_and_value(len,val):
    arr = [val] * len
    return arr

print(length_and_value(4,7))
print(length_and_value(6,2))