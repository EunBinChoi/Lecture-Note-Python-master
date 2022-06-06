#####################################################
################## Python Overview ##################
#####################################################

### [ Python 특징 ] ###

# 1) 동적인 데이터 타입 결정
# why? 파이썬은 모든 데이터 타입이 참조형으로 되어있기 때문
#      어떤 변수든 변수에 담긴 데이터의 주소 (4 bytes) 공간만 스택에서 차지하고 있음
# 2) 파이썬은 인터프리터 언어 (한 줄 읽고 해석해서 실행 (최적화 X)
#    자바는 컴파일 언어 (.java == 컴파일러 최적화 ==> .class)
# 3) 파이썬의 내장함수는 c언어로 구현 (.pyc))
#####################################################

a = 11231241231231241231243241231231235123123123123123123 # int 형의 범위가 없음
print(a)
print(id(a))
print(type(a)) # int

a = 'abasdasd'
print(a)
print(id(a))
print(type(a)) # str

####################################################
# Q1. 두 변수의 주소값은 같을까요? 같음 
# heap 메모리에서 동일한 데이터에 대해서는 같은 주소 할당
# 만약에 객체를 new 하게 되면 다른 주소 할당
# String s1 = new String("abc");
# String s2 = new String("abc");
# &s1 != &s2
# String s3 = "abc";
# String s4 = "abc";
# &s3 == &s4
####################################################

a1 = 300
print(id(a1)) # 1838134264336

a2 = 300
print(id(a2)) # 1838134264336
####################################################

def add(a, b):
    return a + b

print(add(3, 5))       # 숫자 덧셈
print(add('a', 'bc'))  # 문자열 결합
#print(add(3, 'bc'))   # 문자열 결합 X (오류 발생!) 



# 파이썬이 제공하는 내장 함수
# abs(), max(), min(), pow(), chr(), str() ...


# 변수의 생성과 소멸
b = "hello" # 변수 생성
print(b)

del b       # 변수 소멸


# 하나의 변수에 여러 개의 값을 할당하게 되는 경우 tuple로 묶여서 들어가게 됨
h = 1, 2, 3, 4, 5
print(h)
print(type(h)) # tuple

# 왼쪽의 변수의 개수와 오른쪽의 리터럴 값의 개수가 같으면 각각 리터럴이 변수에 대입되서 출력됨
c, d, e, f, g = 1, 2, 3, 4, 5
print(c)
print(d)
print(e)
print(f)
print(g)



#####################################################
##################### Data Type #####################
#####################################################
print(type(1))    # int
print(type(1.1))  # float (double datatype X)
print(type(True)) # bool
print(type('a'))  # str (char datatype X)
print(type("a"))  # str (char datatype X)
print(type([1, 2, 3])) # list (array + linked list)
print(type((1, 2, 3))) # tuple 
print(type({'a' : 1, 'b' : 2, 'c' : 3})) # dict (map)


# str ("abc"), list ([10, 20, 30]), tuple ((10, 20, 30)) (sequence 자료형, 순서가 있는 자료형)
# indexing, slicing (start (0):end (len(s)):step (1))
s = "abc"
print(s[0])   # indexing
print(s[2])   # indexing
#print(s[3])  # indexing (error)
print(s[-1])  # s[len(s)-1]
print(s[-2])  # s[len(s)-2]
print(s[-3])  # s[len(s)-3]
#print(s[-4]) # s[len(s)-4], error 
print(s[1:3]) # "bc", 1 <=   < 3
print(s[1:])  # 1 <=    < len(s)
print(s[:])   # 0 <=    < len(s)
print(s[:2])  # 0 <=    < 2

s = "hello"
# "lo"
print(s[-2:])
print(s[3:])
print(s[::2])
print(s[::-1])

# Q1.
print(end='\n') # enter
print("asdasd", end=' ')
print("asdasdasd")
li = [10, 15, 50, 70, [90, 100, 80]]
# 1) 100 추출
print(li[-1][1])
# 2) [90, 100, 80] 원소 추출
print(li[-1])
# 3) [90, 100, 80] 원소를 추출해서 뒤집기 ([80, 100, 90])
print(li[-1][::-1])
# 4) [10, 15, 50] 원소 추출
print(li[:3]) # 0 <=     < 3

# Q2.
def func(a, b):
    return a, b # 함수의 반환값이 2개 이상 가능 (튜플로 반환)

# 1) res = func(1, 2)을 실행해보고 res 타입 확인해보기
res = func(1, 2) # (1, 2) # tuple packing
print(type(res))
print(res)

# 2) res의 반환값을 c, d에 저장해보기
c, d = res # tuple (1, 2) unpacking
print(c) # 1
print(d) # 2

# 3) res의 반환값 중에 첫번째 원소를 10배 해보기
print(res[0] * 10)

# 4) res의 반환값의 모든 원소를 10배 해보기
print(res * 10)
print(res[0] * 10, res[1] * 10)   # print var args
print(str(res[0] * 10) + " " + str(res[1] * 10)) # ??
print((res[0] * 10, res[1] * 10)) # print tuple

####################################################
print("=" * 100)
# 시퀀스 자료형의 덧셈과 곱셈 연산
# (1, 2) * 10     => 10번 반복
# (1, 2) + (3, 4) => (1, 2, 3, 4) 연결
print((1, 2) * 10)
print((1, 2) + (3, 4))
# print((1, 2) + [3, 4]) # error
print("=" * 100)
####################################################


# Q3.
s = "hello"
# 1) s를 이용해서 "hlo"를 출력
print(s[::2])
# 2) s를 이용해서 "olleh"를 출력
print(s[::-1])
# 3) s를 "Hello"로 변경
s = "H" + s[1:] 
print(s)

####################################################
# 시퀀스 자료형과 dict 지원 함수
# 길이 len(seq)
li = [1, 2, 3]
print(len(li))

dic = {'a':1, 'b':2}
print(len(dic))

# 멤버쉽 테스트 (in, not in)
li = [1, 2, 3]
print(1 in li)

dic = {'a':1, 'b':2}
print('a' in dic.keys()) # key membership test
print(1 in dic.values()) # value membership test
print(dic.keys())    # key만 추출
print(dic.values())  # value만 추출
print(dic.items())   # key, value쌍으로 추출



# list vs tuple
# list : mutable   (수정 가능)
# tuple: immutable (수정 불가)
li = [1, 2, 3]
li[0] = 10 # 가능
tu = (1, 2, 3)
#tu[0] = 10 # 오류

#str = "abc"
#str[0] = "A" # 오류 (수정 불가)

def calculate(a, b):
    return (a+b, a-b, a*b, a/b) # 정수/정수 == 실수

res = list(calculate(3, 4))
print(res)
print(type(res))


# list (sequence datatype ==> indexing, slicing)
# 원소의 datatype이 동일할 필요 X
# array (주소값 연속, 인덱싱 편함) + linked list (원소값 불연속)
# 원소 수정이 가능 (mutable)

li = [1, 2, 3]
print(id(li))
for i in range(len(li)):
    print(li[i], ":",  id(li[i]))

li = [1, 2, 3, 'a', 'b', 4, 5, 6, 'c']
print(li[-1])
print(li[1:3])
print(li[::-1])
print(1 in li) # membership test # O(n)
print(1 not in li) # membership test # O(n)

# 인덱싱이 되어서 어떤 Array에 static하게 저장되어있다는 가정하에 아래의 문제를 풀어보기
print(li[2]) # O(1)
print(li[1:3]) # O(k) (k (j-i) (li[i:j]) <= n)
print(len(li)) # O(1) (인덱싱할 때 전체 원소의 개수를 head에 포함) 

li.append('d') # 리스트의 맨 뒤에 원소 추가 # O(1) 
print(li)

li.insert(3, 4) # 특정 인덱스에 원소 추가 # O(n)
print(li)

li = ['a', 'b', 'c', 1, 'a', 10]
li.remove(1)    # 삭제하려고 하는 원소 값 지정 # O(n)
print(li)

li = [1, 'b', 1, 'c', 1, 'a', 10]
li.pop()        # 만약 인자가 없으면 맨 뒤에 있는 원소 삭제 # O(1)
li.pop(1)       # 인자가 있으면 인자로 주어진 인덱스의 원소 삭제 # O(n)
print(li)

li = [1, 'b', 1, 'c', 1, 'a', 10]
del li[1]      # 해당 인덱스의 원소 삭제 # O(n)

# append vs extend
li1 = [1, 2, 3]
li2 = [4, 5, 6]
li1.append(li2)
print(len(li1))
print(li1) # [1, 2, 3, [4, 5, 6]]: len(): 4
print(li1[3])
print(li1[3][2])

li1 = [1, 2, 3]
li2 = [4, 5, 6]
li1.extend(li2)
print(len(li1))
print(li1) # [1, 2, 3, 4, 5, 6]: len(): 6
print(li1[3])
print(li1[-1])

li1 = [1, 2, 3]
li2 = [4, 5, 6]
li3 = li1 + li2
print(li3)