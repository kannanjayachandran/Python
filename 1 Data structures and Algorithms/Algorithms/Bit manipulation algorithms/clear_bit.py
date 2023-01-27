def clear_bit(num: int, k: int)->int:
    """
    Method Name: clear_bit
    
    Purpose: To clear the k-th bit of a number 

    Output: Resulting number after clearing the k-th bit
    """
    return num & (~(1<<k))


if __name__ == '__main__':

    num = int(input('Enter the num: '))
    k = int(input("Enter the value of 'k': "))

    print(f'The num{num} after clearing the {k}-th bit is {clear_bit(num, k)}')