def bubble_sort(arr: list[int]) -> list[int]:
    """Application of bubble sort algorithm using for loops"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    # ChatGPT code, similar to my logic but from the largest to smallest
    # n = len(arr)
    # for i in range(n):
    #     for j in range(0, n-i-1):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    """Basic implementation of sort in python using sorted or sort function"""
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    # print(sorted(sample_array))
    # sample_array.sort()
    # print(sample_array)

    """With Bubble sort algorithm"""
    print(bubble_sort(sample_array))