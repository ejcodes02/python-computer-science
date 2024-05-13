def main():
    size = get_size()
    pyramid(size)

def pyramid(size):
    space = size
    for row in range(size + 1):
        print(" " * space, end="")
        print(f"{row} " * row)
        space -= 1

def get_size():
    while True:
        try:
            num = int(input("Specify the dimensions: "))
        except ValueError:
            print("Invalid input")
        else:
            return num

if __name__ == "__main__":
    main()