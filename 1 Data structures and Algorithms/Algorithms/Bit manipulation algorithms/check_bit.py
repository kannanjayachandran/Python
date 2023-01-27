def check_bit(num: int, k: int)->bool:
    """
    Method Name: check_bit
    
    Purpose: To check whether the k-th bit of a number is set or not

    Output: True or False
    """
    return bool(num & (1<<k))


if __name__ == '__main__':

    num = int(input('Enter the num: '))
    k = int(input("Enter the value of 'k': "))

    print(f'The {k}-th bit of {num} is {check_bit(num, k)}')


# Time complexity : O(1)

# Space complexity : O(1)