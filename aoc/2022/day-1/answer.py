with open('./data.txt', 'r') as f:
    cal = [int(i) for i in f.read().strip().split('\n') if i]

a = [sum(cal[i:i+3]) for i in range(0, len(cal), 3)]
a.sort(reverse=True)

print(a[0]) # 1st answer
print(sum(a[:3])) # 2nd answer
