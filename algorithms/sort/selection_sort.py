def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr[:-1])):
        # x is the minimum index
        x = i
        for j in range(i+1, len(arr)):
            if arr[x] > arr[j]:
                x = j
        arr[i], arr[x] = arr[x], arr[i]

    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(selection_sort(arr))