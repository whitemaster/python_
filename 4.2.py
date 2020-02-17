import random
def sum(arr, number):
    sum_0 = 0
    sum_1 = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                sum_0 += arr[i][j]
            if i+j+1 == len(arr):
                sum_1 += arr[i][j]
    if number == 0:
        sum = sum_0
    else:
        sum = sum_1
    return sum


print("Write the size of matrix")
n = int(input())
arr = []
for i in range(0, n):
    now_arr = [random.randint(0, 100) for _ in range(n)]
    arr.append(now_arr)
for i in range(0, n):
    print(arr[i])
print("What diagonal of matrix you want sum? Main - 0, Side - 1")
answer = int(input())
print(sum(arr, answer))
