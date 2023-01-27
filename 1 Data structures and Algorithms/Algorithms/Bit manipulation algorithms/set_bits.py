def set_bits(num: int, k: int)->int:
    """
    Method Name: set_bit
    
    Purpose: To set the k-th bit of a number

    Output: Resulting number after setting the k-th bit
    """
    return num | (1<<k)


if __name__ == '__main__':

    num = int(input('Enter the number : '))
    k = int(input("Enter 'K' : "))

    print(f'The num {num} after setting {k}-th bit is : {set_bits(num, k)}')



# Time complexity : O(1)

# Space complexity : O(1)
