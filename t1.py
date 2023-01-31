def sum_elem(arr, s):
    for i in range(len(arr)-1):
        if s - arr[i] in arr[i:]:
            t = arr.index(s - arr[i])
            if arr[i] <= arr[t]:
                return f'{arr[i]} {arr[t]}'
            else:
                return f'{arr[t]} {arr[i]}'
    return None


def sum_elem1(arr, s):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == s:
                if arr[i] <= arr[j]:
                    return f'{arr[i]} {arr[j]}'
                else:
                    return f'{arr[j]} {arr[i]}'
    return None

# a, s, _ = ([5, 4, 3, 2, 1], 8, '3 5')
# print(sum_elem(a, s))
