# i = 0
# for i in range(11):
#     print(i)
#     i += 1
#
# for i in range(10, -1, -1):
#     print(i, end=' ')
#
#
# for i in range(-10, -1, 2):
#     print(i, end=' ')
#
# for i in range(1, 20, 3):
#     print(i, end=' ')
#
# n = list(map(int, input().split()))
# total = 0
# for i in range(len(n)):
#     if n[i] % 2 != 0:
#         total += n[i]
#         print(total)
#
#
# cityes = input().split()
# for i in range(len(cityes)):
#     print(len(cityes[i]), end=' ')
#
#
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=' ')
#
# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     if n != 1 and n % i == 0:
#         count += 1
# if count == 2:
#     print('YES')
# else:
#     print('NO')
#
#
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
#
# n = int(input())
# total = 0
# for i in range(n):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
# print(total)
#
# phrase = input().lower()
# for i, d in enumerate(phrase):
#     if d == 'р' and phrase[i + 1] == 'а':
#         print(i)
# else:
#     print(-1)
#
# Барабанщик бил бой в барабан
#
#
# objs = iter([23, 78, True, 'hello', [123, 433]])
# print(next(objs))
# print(next(objs))
# print(next(objs))
#
#
# for i in range(0, 505, 5):
#     print(i)
#
# total = 0
# for i in range(50, 101):
#     i **= 3
#     total += i
# print(total)
#
#
# n = int(input())
# for i in range(n):
#     s = input()
#     if len(s) > 10:
#         print(s[0] + str(len(s[1:-1])) + s[-1])
#     else:
#         print(s)
#
#
# numbers = [99, 50, -16, 9, 47, -62, 5, -64, -68, 85, 11, -20, 16, 96, -43, 46, -25, 33, 81, -30, 64, 66, -11, 60, 3, -5, -1,
#            -80, 49, -12, -86, -40, -98, -92, -91, -71, 56, -76, -30, -
#            82, 17, -2, -64, 47, 22, -28, 40, 55, 54, -3, -58, -10,
#            -35, -15, -2, -60, 70, 50, -77, 83, -49, 42, 27, -58, -
#            79, -2, -100, -42, -18, 38, 95, 9, 98, -89, -46, 96, 64,
#            -35, 41, 94, 1, -90, 29, 23, 39, -3, 11, -65, -64, 52, -69, 32, -14, -49, -28, -11, 85, -75, -6, 15]
# for i in numbers:
#     print(i)
#
#
# words = ['require', 'build', 'head', 'land', 'dark', 'seat', 'have', 'five', 'particularly', 'focus', 'moment',
#          'visit', 'past', 'turn', 'bad', 'modern', 'once', 'future', 'pay', 'assume', 'himself', 'physical', 'chance',
#          'remember', 'better', 'former', 'believe', 'explain', 'reduce', 'whatever', 'theory', 'during', 'enough',
#          'wall', 'commercial', 'challenge', 'tell', 'actually', 'include', 'somebody', 'decade', 'by', 'better',
#          'would', 'five', 'cost', 'kitchen', 'our', 'affect', 'board', 'practice', 'full', 'instead', 'apply', 'good',
#          'past', 'clearly', 'special', 'both', 'analysis', 'peace', 'truth', 'cultural', 'light', 'answer', 'build',
#          'each', 'watch', 'buy', 'theory', 'pretty', 'expect', 'account', 'music', 'sell', 'newspaper', 'reach',
#          'fish', 'tax', 'employee', 'start', 'most', 'during', 'citizen', 'develop', 'carry', 'only', 'certainly',
#          'rock', 'economy', 'risk', 'later', 'one', 'body', 'star', 'they', 'choice', 'appear', 'return', 'sometimes']
# for i in words:
#     if len(i) > 6:
#         print(i)
#
#
# n = list(map(int, input().split()))
# num = int(input())
# for i in n:
#     if num == i:
#         print(n.index(i) + 1)
#         break
# else:
#     print('ErrorValue')
#
#
# n = map(int, input().split())
# num = int(input())
# count = 1
# for i in n:
#     if num == i:
#         print(count)
#         break
#     count += 1
# else:
#     print('ErrorValue')
#
#
# s = input().split()
# smallest = 1000000000000000



# count = 0
# for i in range(len(s)):
#     if 0 < int(s[i]) < smallest:
#         smallest = int(s[i])
#         count += 1
# if count > 0:
#     print(smallest)
# else:
#     print('Empty')
#
#
# s = input()
# count = 0
# for i in s:
#     print(s[i])
#     if s[0] == ')':
#         count += 1
#         break
#     if i % 2 != 0 and i == '(':
#         count += 1
#     else:
#         count -= 1
# if count == 0:
#     print('YES')
# else:
#     print('NO')
#
# 8 11 45 32 543 65
# # 32


print('change')
print('change')
print('change')
print('change')
print('change')
print('change')
print('change')
print('change')
print('change')
print('change')
print('change')
print('change')