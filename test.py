# i = 0
# for i in range(11):
#     print(i)
#     i += 1

# for i in range(10, -1, -1):
#     print(i, end=' ')
#


# for i in range(-10, -1, 2):
#     print(i, end=' ')

# for i in range(1, 20, 3):
#     print(i, end=' ')

# n = list(map(int, input().split()))
# total = 0
# for i in range(len(n)):
#     if n[i] % 2 != 0:
#         total += n[i]
#         print(total)



# cityes = input().split()
# for i in range(len(cityes)):
#     print(len(cityes[i]), end=' ')


# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=' ')

# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     if n != 1 and n % i == 0:
#         count += 1
# if count == 2:
#     print('YES')
# else:
#     print('NO')




# cities = input().lower().split()
# prev = cities[0][-1]
# for i in range(1, len(cities)):
#     if prev == 'ы' or prev == 'ъ' or prev == 'ь':
#         prev = cities[i - 1][-2]
#     if prev == cities[i][0]:
#         answer = 'ДА'
#     else:
#         answer = 'НЕТ'
#         break
#     prev = cities[i][-1]
# print(answer)
#
# # data = input().lower().split()
# # result = 'ДА'
# # for i in range(1, len(data)):
# #     if data[i][0] != data[i - 1].rstrip("ьъы")[-1]:
# #         result = 'НЕТ'
# # print(result)

# n = int(input())
# total = 0
# for i in range(n):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
# print(total)

# phrase = input().lower()
# for i, d in enumerate(phrase):
#     if d == 'р' and phrase[i + 1] == 'а':
#         print(i)
# else:
#     print(-1)

# Барабанщик бил бой в барабан


objs = iter([23, 78, True, 'hello', [123, 433]])
print(next(objs))
print(next(objs))
print(next(objs))