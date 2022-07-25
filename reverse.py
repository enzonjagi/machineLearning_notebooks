from audioop import reverse
from ntpath import join


def reverse_string(name):
    n = []
    for i in name:
        n.append(i)
        reversed = []
        reversed = n[-1:0]
    return (str(reversed))


name = reverse_string("Njagi")


def reverse_str(name):
    reversed = []
    i = len(name) - 1
    while (i >= 0):
        reversed.append(name[i])
        i -= 1
    return (''.join([str(x) for x in reversed]))


name2 = reverse_str("Njagi is dangerous")
print(name)
print(name2)
