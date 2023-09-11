def binarySearch(arr: list[int], target: int) -> int:
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1

        elif arr[mid] < target:
            start = mid + 1

    return -1


if __name__ == "__main__":
    userIn = input("Enter numbers separated by comma {Sorted}:\n").strip()
    arr = [int(x.strip()) for x in userIn.split(",")]

    target = int(input("Enter the number to search:\n").strip())

    result = binarySearch(arr, target)

    if result != -1:
        print(f"The element {target} is found at index {result}.")

    else:
        print(f"Element {target} was not found in {arr}.")
