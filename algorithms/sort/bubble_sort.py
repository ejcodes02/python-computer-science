def main():
    """Basic implementation of sort in python using sorted or sort function"""
    sample_array = [2, 1, 5, 4, 3]
    print(sorted(sample_array))
    sample_array.sort()
    print(sample_array)

    """Utilizes for loops to sort the int array"""
    sample_array = [2, 1, 5, 4, 3]
    for i in range(len(sample_array)):
        for j in range(i + 1, len(sample_array)):
            x = sample_array[i]
            y = sample_array[j]
            if x > y:
                sample_array[i] = y
                sample_array[j] = x

    print(sample_array)

if __name__ == "__main__":
    main()