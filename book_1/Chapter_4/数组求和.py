def sum_array(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

def sum_aray1(arr):
    sum = 0
    k = 0
    size = len(arr)
    while k < size:
        sum += arr[k]
        k += 1
    return sum

test_arrays = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
               [2.5, 3.5, 7.8, 5.6],
               [0],
               [-1, -2, -3, -4, -5, -6],
               [],
               ]
# for test_array in test_arrays:
#     result = sum_array(test_array)
#     print(result)

for test_array in test_arrays:
    result = sum_aray1(test_array)
    print(result)