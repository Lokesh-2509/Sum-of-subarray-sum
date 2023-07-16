def sum_of_all_subarray_sums(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        total_sum += arr[i] * (i + 1) * (n - i)
    return total_sum
A1 = [1, 2, 3]
print(sum_of_all_subarray_sums(A1))

A2 = [2, 1, 3]
print(sum_of_all_subarray_sums(A2))
