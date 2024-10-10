x = 5
y = 10

target = x+y
print("total is ", target)

list = [1,2,3]
target = 0

n = len(list)
print (n)
for i in range(n-1):
    for j in range(i+1,n):
        if list[i]+list[j] == target:
            print([i,j])
print([])

        