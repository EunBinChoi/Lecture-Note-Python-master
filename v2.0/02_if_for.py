import math

# 파이썬은 {} (블럭) 개념이 없고 들여쓰기로 구분

print("hello")
print("hello")

# if문
a = 10
if a > 90:     
    print("A")
elif a > 80: 
    print("B")
elif a > 70: 
    print("C")
elif a > 60: 
    print("D")
else: 
    print("F")

# for문
# 파이썬에서 for문은 for-each문
# i 조작이 어려움
li = list(range(10)) # [start(0):stop(len(s)):step(1)]
print(li)

for i in range(len(li)):
    if(i == 5): i = 2
    print(i)

# 이럴 경우에는 for 대신 while 사용

# i = 0
# while(i < len(li)):
#     if(i == 5): i = 2
#     print(i)
#     i += 1

li = [10, 20, 30]
for i in range(len(li)): # 0 <=   < 10
    print(li[i])

for ele in li: # 0 <=   < 10
    print(ele) 

for i, ele in enumerate(li):
    print(i, ":", ele) 

i = 0 # global
for i in range(10):
    #if i % 2 == 1:
    #    break
    print(i)

# range(10) == [0, 1, 2, .. 9]
if(i == list(range(10))[-1]): print("non-break")
else: print("break")


for i in range(10):
    #if i % 2 == 1: break
    print(i)
else: # for문이 정상적으로 (중간에 break 되지 않고) 모두 실행되면
    print("asdasd : non-break") # 아래 문장이 실행됨

#  Q1. for-else 문제
# membership test (in) ==> True, False

def membership(li, element):
    for ele in li:
        if(ele == element): return True
    else: return False

li = list(range(10))
isMember = membership(li, 3) # bool
print(isMember)

# Q2. 사용자에게 값을 입력받아 해당 값이 소수인지 아닌지 판별하는 함수
"""
System.out.print("number? ");
int number = scanner.nextInt();
"""
number = int(input('number ? '))
print(number)
print(type(number))

# 1) 1 ~ number count == 2
# 2) 2 ~ number-1 
# 3) 에라토스테네스의 체
def isPrime1(number):
    count = 0
    for i in range(1, number + 1): # 1 <=  < number + 1
        if number % i == 0: count += 1
    if count == 2: return True
    else: return False
print("prime number" if isPrime1(number) else "not prime number")

def isPrime2(number):
    for i in range(2, number): # 2 <=  < number
        if number % i == 0: return False
    return True
print("prime number" if isPrime2(number) else "not prime number")


def isPrime3(number):
    for i in range(2, int(math.sqrt(number)) + 1): # 2 <=  < number
        if number % i == 0: return False
    return True
print("prime number" if isPrime3(number) else "not prime number")



for i in range(10):
    if i % 2 == 1: continue
    print(i)


# Q1. 
s = "1, 2, 3, 4"
li = []
temp = ""
for i in range(len(s)):
    if(s[i] == ","):
        li.append(temp.strip())
        temp = ""
    else:
        temp += s[i]
li.append(temp.strip())
print(li)
        

# Q2. Sally의 비밀 채팅방 (hELLO wORLD) 
s = "hello world"
res = ""
for i in range(len(s)):
    if(i == 0 or s[i-1].isspace()):
        res += s[i].lower()
    else:
        res += s[i].upper()
print(res)


# Q3. 
li = list(range(1, 5))
s = ""

for i in range(len(li)):
    s += str(li[i]) + ", "
s = s.strip()[:-1]
print(s)