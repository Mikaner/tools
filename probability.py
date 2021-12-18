def calc(per, num):
    sum_data = 0
    remain = 1
    for i in range(num):
        data = remain*per
        sum_data += data
        remain -= data
    return sum_data, remain

print(calc(0.99,10000000))

