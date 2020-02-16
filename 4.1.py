import random


def generation_arr(arr):
    arr = [random.randint(0,100) for _ in range(5)]
    return arr
def sum(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum


if __name__ == '__main__':
    arr = []
    max_sum = 0
    all_arr = []
    max_arr = []
    arr_1 = generation_arr(arr)
    all_arr.append(arr_1)
    arr_2 = generation_arr(arr)
    all_arr.append(arr_2)
    arr_3 = generation_arr(arr)
    all_arr.append(arr_3)
    arr_4 = generation_arr(arr)
    all_arr.append(arr_4)
    arr_5 = generation_arr(arr)
    all_arr.append(arr_5)
    arr_6 = generation_arr(arr)
    all_arr.append(arr_6)
    arr_7 = generation_arr(arr)
    all_arr.append(arr_7)
    arr_8 = generation_arr(arr)
    all_arr.append(arr_8)
    arr_9 = generation_arr(arr)
    all_arr.append(arr_9)
    arr_10 = generation_arr(arr)
    all_arr.append(arr_10)
    for arr in all_arr:
        print(arr)
        print(sum(arr))
    number = 0
    max_number = 0
    for i in all_arr:
        number +=1
        if sum(i) > max_sum:
            max_sum = sum(i)
            max_arr = i
            max_number = number
    print(max_number)
    print(max_sum)
    print(max_arr)