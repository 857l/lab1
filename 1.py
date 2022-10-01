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

s = ''
for i in a:
    s += str(i) + ' '

f = open('output.txt', 'w')
f.write(s)
f.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
