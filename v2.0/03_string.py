"""
string, list, tuple (sequence datatype)
sequence: indexing을 통해 원소를 접근
- 공통 연산: indexing, slicing, +, *, in/not in, len(), for ~ in

list: mutable (원소 수정 가능)
string, tuple: immutable (원소 수정 불가, 상수적 특징이 있음)
"""

#li = [1, 2, 3] # list
#li[0] = 10

tu = (1, 2, 3) # tuple
li = list(tu)  # tuple -> list
li[0] = 10
print(li)
#tu[0] = 10 # error

s = "hello" # string
s = "H" + s[1:]
print(s)
#s[0] = "H" # error

# +
li = [1, 2, 3] + [4, 5, 6]
print(li)

tu = (1, 2, 3) + (4, 5, 6)
print(tu)

s = "h" + "ello"
print(s)

#s = 1 + "2" # error
#print(s)

# *
li = [1, 2, 3] * 10
print(li)

tu = (1, 2, 3) * 10
print(tu)

s = "=" * 10
print(s)

# membership test (in, not in)
li = [1, 2, 3]
print(10 in li)
print(10 not in li)

tu = (1, 2, 3)
print(10 in tu)
print(10 not in tu)

s = "hello"
print("h" in s)
print("h" not in s)

# len()
print(len(li))
print(len(tu))
print(len(s))

########################################################
# string
s = 'h' # python char형이 없음
s = "h"
s = 'asdasdasdasdasdadasdasdasdasdasdasdasdasd\
asdasdasdasdasdasdsadasdasdasd\
asdasdasdasdasdasdasdasdasdasd'
s = '''asdasdasdasdasdasdsadas
dasdasdasdasdasd
asdasdasdasd'''

# string method
s = 'python is fun'
print(s.upper())
print(s.lower())
print(s.capitalize()) # 시작하는 첫 문자만 대문자
print(s.title()) # 각 단어의 시작 첫 문자를 대문자

s = 'i like python, i love python'
print(s.count('python'))
print(s.find('python'))
print(s.startswith('python'))
print(s.endswith('python'))

# window os: \r\n (enter)
# unix os: \n (enter)
s = "    \t \n    dsads    \t \n \r     ".strip() # white space
print(s)

# strip 안의 문자가 해당 문자열 안에 양 옆에 있을 경우 삭제
# 만약 더이상 연속적이지 않는 경우에는 삭제를 멈춤
s = "><><><><><><asd<>asdsad><><><><><><".strip('<>')
print(s)

s = "abc adc aaa".replace('a', 'q') # replace all
print(s)

# "a b c d" => ['a', 'b', 'c', 'd']
li = "a b c d".split() # white space
print(li)

# ['a', 'b', 'c', 'd'] => "a b c d"
li = ['a', 'b', 'c', 'd']
st = " ".join(li)
print(st)

print("=" * 60)
# Q1. ['a', 'b', 'c', 'd'] (list)로 바꾸기
li = "a, b, c, d".split(', ')
print(li)

li = "a, b, c,d".replace(' ', '').split(',')
print(li)


# Q2. li_s를 "abcd" (str)로 바꾸기
li = ['a', 'b', 'c', 'd']
li_s = str(li)
s = ""
for i in range(len(li_s)):
    if 'a' <= li_s[i] <= 'z':
        s += li_s[i]
print(s) 

# Q3.
dic = {'a':1, 'b':2, 'c':3} # sequence datatype 아님
print(dic['a'])
print(dic['b'])
print(dic['c'])
#dic['a'] = 10
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic.items()))

# 1) 'abc' 반환
s = "".join(list(dic.keys())) # ['a', 'b', 'c'] => "abc"
print(s)

# 2) '123' 반환
# list comprehension (리스트 내포법)
# [1, 2, 3] => ['1', '2', '3']
s = "".join([str(ele) for ele in list(dic.values())]) 
print(s)

li = []
for ele in list(dic.values()):
    li.append(str(ele))
s = "".join(li)

# join (join 하려고 하는 리스트의 원소가 str)
li = [1, 2, 3]
s = "" # result
sp = " " # spliter (delimiter)
#for el in li:
    #s += el + sp # error


# java style
values = list(dic.values())
values__str = []
for ele in values:
    values__str.append(str(ele))
s = "".join(values__str)
print(s)


# 3) '23' 반환
s = "".join([str(ele) for ele in list(dic.values())])[1:]
print(s)

# 4) 'ab' 반환
s = "".join(list(dic.keys()))[:-1]
print(s)

# 5) 'a1 b2 c3' 반환
print(list(dic.items()))
s = ""
for key, value in dic.items():
    s += str(key) + str(value) + " "
print(s)

s = " ".join([str(key) + str(value) for key, value in dic.items()])
print(s)


# list comprehension
li = [1, 2, 3]
alphabets = "abc"

res = []
for e in li:
    for s in alphabets:
        res.append(str(e) + str(s))
print(res)

res = [str(e) + str(s) for e in li for s in alphabets]
print(res)

# Q1. range(10)에서 홀수들만 선별하여 해당 수를 제곱해서 리스트에 포함
li = [num**2 for num in range(10) if num % 2]
print(li)

# num*num == num**2 == pow(num, 2)

# True: 0이 아닌 모든 값 (대표값: 1)
# False: 0
print(bool(1)) # True
print(bool(-1)) # True
print(bool(-100000)) # True
print(bool(0)) # False
print(bool("")) # False
print(bool(" ")) # True
print(bool(None)) # False
print(bool([])) # False
print(bool(())) # False
print(bool({})) # False
print(not bool(None)) # True
print(True + 1) # 2

li = ['a','a','a','a','a','a','a','a','a', ['a','a','a','a','a']]
print(len(li)) # 1
print(li[0][0])

# Q2. 아래의 문자열에서 [("hello", 5), ("world!", 6) ....]
s = "hello world! this is python world!"
li = [(s, len(s)) for s in s.split()]
print(li)
print(li[0])
print(li[1])


# java style
li = []
tmp = ""
for i in range(len(s)):
    if(s[i] == ' '):
        li.append((tmp, len(tmp)))
        tmp = ""
    else: tmp += s[i]
li.append((tmp, len(tmp)))
print(li)


# list append (add), = (set)
li = ["" for _ in range(10)]
print(li)

li = []
for _ in range(10):
    li.append("")


# string formatting
name = "sally"
age = 30
print('name = %s, age = %d' % (name, age))
print('name = {0}, age = {1}'.format(name, age))

full = 'I am {0}'.format(name)
print(full)

############################################
letter = '''이 편지는 영국에서 시작되어 .....
{0}님 이 편지를 10번 공유하지 않으면 ........

from 영국 젠틀맨'''

names = ['이씨', '박씨', '김씨']

for name in names:
    print(letter.format(name))
