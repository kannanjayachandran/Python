def linearSearch(arr: list[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


if __name__ == "__main__":
    userIn = input("Enter numbers separated by comma:\n").strip()
    arr = [int(x.strip()) for x in userIn.split(",")]

    target = int(input("Enter the number to search:\n").strip())

    result = linearSearch(arr, target)

    if result != -1:
        print(f"The element {target} is found at index {result}.")

    else:
        print(f"Element {target} was not found in {arr}.")
