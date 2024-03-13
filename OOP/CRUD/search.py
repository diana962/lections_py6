ls = [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 15, 16, 17, 23]
left = 0 # индекс первого числа
right = len(ls) - 1 # с этим мы находим число id
# print(right)
# print(ls[right])
# -----------------------
# last_index = ls.index(23)
# print(last_index) # 13
# -----------------------

mid = len(ls) // 2 # индекс среднего числа
value = int(input('Enter a number in range(0, 23): ')) # мы установили число для поиска

count = 0
while ls[mid] != value and left <= right:
    if value < ls[mid]:
        right = mid - 1
    else:
        left = mid + 1
    mid = (left + right) // 2
    count += 1
print(count)

if left > right:
    print('Not Found')
else:
    print(f'{value} = {ls[mid]} id: {mid}')


