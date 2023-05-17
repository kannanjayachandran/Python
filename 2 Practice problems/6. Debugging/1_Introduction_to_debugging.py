import pdb


def print_seq(n: int):
    for i in range(n):
        # set a breakpoint and we can access different vars
        pdb.set_trace()
        print(i)

print_seq(5)

# h : list all the debugging commands
