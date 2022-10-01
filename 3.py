import time

def fun(arr, n):
    if n <= 1:
        return

    fun(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = last

    return arr


t_start = time.perf_counter()
f = open('input.txt', 'r')
x = int(f.readline())
a = [0] * x
x = f.readline()

a = x.split()
for i in range(len(a)):
    a[i] = int(a[i])

a = fun(a, len(a))

s = ''
for i in a:
    s += str(i) + ' '

f = open('output.txt', 'w')
f.write(s)
f.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
