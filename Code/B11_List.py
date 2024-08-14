ds = [1,2,3,4,5,6,7,8,9,10]
ds.append(1)

n = int(input())
lap = range(0, n)

for x in lap:
    ds.append(input())

print(ds)