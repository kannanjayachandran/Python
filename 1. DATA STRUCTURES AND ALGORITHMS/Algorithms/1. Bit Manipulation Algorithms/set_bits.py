

def set_bits(num: int, k: int)->int:

    return num | (1<<k)


if __name__ == '__main__':

    num = int(input('Enter the number : '))
    k = int(input("Enter 'K' : "))

    print(f'The num {num} after setting {k}-th bit is : {set_bits(num, k)}')



# Algorithm : To set the k-th bit of a number

# Time complexity : O(1)

# Space complexity : O(1)
