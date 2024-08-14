print("Nhap vao so luong phan tu cua mot danh sach")
n = int(input())
ds = []

for x in range(0, n):
    ds.append(int(input()))

a = 0;

for x in range(0, n):
    if(x > a):
        a = x

print(a)