'''
     Print the following pattern.
     *
     * *
     * * *
     for given 'n = 3'
'''

n = int(input("Enter the number: "))

for i in range(0, n+1):
    for j in range(0, i):
        print("* ", end='')
    print()
