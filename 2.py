import time

t_start = time.perf_counter()

f = open('input.txt', 'r')
x = int(f.readline())
a = [0] * x
x = f.readline()
a = x.split()

for i in range(len(a)):
    a[i] = int(a[i])

for i in range(len(a) - 1):
    j = i + 1
    while j > 0:
        if a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break
        j -= 1

s1 = ''
for i in a:
    s1 += str(i) + ' '
s1 += '\n'

s2 = ''
for i in range(len(a)):
    s2 += str(i) + ' '

f = open('output.txt', 'w')
f.write(s1)
f.write(s2)
f.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
