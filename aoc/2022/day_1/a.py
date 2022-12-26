with open('./c.txt', 'r') as f:
    cal = [i for i in f.read().strip().split('\n')]

a = []
count = 0
num = 0

for item in cal:
    
    if item != '':
        num = int(item)
        count += num

    else:
        a.append(count)
        count = 0

a.append(count)
a.sort(reverse=True)

print(a[0]) # 1st answer
print(a[0]+a[1]+a[2]) # 2nd answer