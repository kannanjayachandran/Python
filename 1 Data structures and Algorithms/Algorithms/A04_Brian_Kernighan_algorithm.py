def brk_algo(num: int)->int:

    ans = 0
    while (num>0):
        num &= num - 1
        ans = ans + 1

    return ans


if __name__ == '__main__':

    num = int(input('Enter the num: '))

    print(f'Number of set bits in {num} is {brk_algo(num)}')