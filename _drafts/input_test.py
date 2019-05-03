import sys
for line in sys.stdin:
    print([ord(x)-48 for x in line.split()])

print('input end')
