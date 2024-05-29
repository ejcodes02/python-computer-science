def linear_search(arr: list[int], target: int) -> int:
    for idx, i in enumerate(arr):
        if i == target:
            target_idx = idx
            break
    return target_idx

if __name__ =="__main__":
    arr = [1, 4, 5, 7, 9, 12, 15, 18, 19, 22, 25, 29, 40, 50]
    target = 12
    print(f"Target index: {linear_search(arr, target)}")