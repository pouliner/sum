
f = open('/home/polyak/PycharmProjects/test1/Romanych/input/task0.in')
str1 = str(f.readline())
str2 = str(f.readline())
str1 = str1[:-1]
str2 = str2[:-1]
str1 = str1[::-1]
str2 = str2[::-1]

str_max = []
f.close()
f = open('/home/polyak/PycharmProjects/test1/Romanych/output/task0.out')
check = f.readline()
f.close()
print(check)

if len(str1) > len(str2):
    str_max = str1.copy()
    str1 = str2.copy()
    str2 = str_max


l1 = len(str1)
l2 = len(str2)
str_summ = []
remainder = 0
divider = 10
for k in range(l1):
    summ = int(str1[k]) + int(str2[k]) + remainder
    str_summ.append(summ % divider)
    remainder = summ // divider
for k in range(l1, l2):
    summ = int(str2[k]) + remainder
    str_summ.append(summ % divider)
    remainder = summ // divider
# if (remainder):
#     str_summ.append(remainder)
str_result = ""
str_summ = str_summ[::-1]

u = list(map(str, str_summ))
for y in range(len(u)):
    str_result = str_result + u[y]


f = open('/home/polyak/PycharmProjects/test1/Romanych/output/task0.out', 'w')
f.write('ответ:  ')
f.write(str_result)
f.close()

print(str1)
print(str2)

print(str_result)
print((check == str_result))
