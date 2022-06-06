#-*- coding: euc-kr -*-#
# python�� �鿩���� �ΰ��� ���

a = 1
# a = 1

# if() {
#   // block
# 
# }

# if��
score = 90
if score >= 90:
    print('A! pass! congrat!')
elif score >= 80:
    print('B!')
elif score >= 70:
    print('C!')
else:
    print('fail!')


# for�� (for each�� �� �� ����)
li = ['a', 'b', 'c']
for i in li:
    print(i)

# for�� + range()
######################################################
# range(start, stop, step)
# range(stop)
# range(start, stop)
# default: start - 0, stop - len(), step - 1
######################################################
print(range(10))
print(list(range(10))) # 0 ~ 10-1
print(list(range(1, 10))) # 1 ~ 10-1
print(list(range(1, 10, 2))) 
# 1 ~ 10-1 (2ĭ�� �ǳʶٸ�)
# 1 3 5 7 9

# 1 ~ 10 ����
sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

# for each
li = ['a', 'b', 'c']
for i in li:
    print(i)

# for using index
for i in range(len(li)): # 0 ~ 2
    print(li[i]) 

# for + enumerate() : �ε��� + ���� �� �Բ� ��ȯ
for i, al in enumerate(li):
    print(i, ":", al)

# break, continue

for i in range(1, 11):
    if(i % 3 == 0): continue
    print(i) 

# for ~ else: for���� ���������� ��� ����Ǹ� else ���� ����
# (�߰��� break�� ���ؼ� for���� �ߴܵ��� ������)
li = [1, 2, 4, 20, 6]
for i in li:
    if(i > 10): break
    print(i)
else:
    print('else block')

# 1)
# �� ����Ʈ�� ���Ұ� �������� Ȯ��
li1 = [10, 20, 30, 40, 50]
li2 = [10, 20, 30, 30, 50]

# 1. ����Ʈ�� ���̰� �ٸ��� �������� ����
# 2. ����Ʈ�� ���� �ϳ��� ���ؾ���

def listEquals(li1, li2):
    if(len(li1) != len(li2)): return False

    for i in range(len(li1)):
        if(li1[i] != li2[i]): return False
    else: return True

print(listEquals(li1, li2))
print(listEquals(li1, li2))

# 2) 2 ~ 9�� ������ ���
for i in range(2, 10): # 2 ~ 9
    for j in range(1, 10): # 1 ~ 9
        print(i, '*', j, '=', i * j)
        #print(str(i) + '*' + str(j) + '=' + str(i * j))
    print()

for i in range(2, 10):
    for j in range(1, 10):
        print("{0} * {1} = {2}".format(i, j, i * j))
    print()

for i in range(2, 10):
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i * j))
    print()


# while��
# �ʱ�ȭ, ���ǽ�, ������
sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum)

# while ~ else��
sum = 0
i = 1
while i <= 10:
    if(i == 5): break
    sum = sum + i
    i = i + 1
else:
    print('else block')

print(sum)
