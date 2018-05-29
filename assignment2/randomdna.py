from random import randint

length = input('Length: ')
lNC = ['A','C','T','G']

print '>randomsequence%s' %length
print ''.join([lNC[x] for x in [randint(0,3) for x2 in range(length)]])

