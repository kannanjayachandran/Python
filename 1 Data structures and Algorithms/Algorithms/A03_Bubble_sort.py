def bubble_Sort(arr: list[int], length: int) -> list[int]:
    for i in range(length):
        swapped = False

        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    userIn = input("Enter numbers separated by comma:\n").strip()
    arr = [int(x.strip()) for x in userIn.split(",")]

    length = len(arr)

    print(f"The sorted sequence is:", bubble_Sort(arr, length))
