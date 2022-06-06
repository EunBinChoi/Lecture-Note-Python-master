# 파일 입출력

import os
print(os.getcwd()) # current working directory
print(os.listdir('.'))
print(os.listdir('..')) 
#os.mkdir('temp')
#os.rename('temp', 'temp2')

# 파일 처리
# 1) 읽기 'r' (read)
# 2) 쓰기 'w' (write)
# - 파일이 없는 경우에는 새로운 파일을 생성해서 작성
# - 파일이 있는 경우에는 이미 존재하는 내용물을 없애고 작성
# 3) 파일 끝에 추가 'a' (append)
# - 파일이 없는 경우에는 새로운 파일을 생성해서 작성
# - 파일이 있는 경우에는 이미 존재하는 내용물 끝에 작성

# file rename policy
def renameFile(f):
    i = 1
    loc = f.rfind('.') # find right (extend)
    name = f[:loc]
    extend = f[loc:]
    while(os.path.exists(f)):
        rename = name + str(i)
        f = rename + extend
        i += 1
    return rename + extend

# os.path.exists()
# test.txt -> test1.txt -> test2.txt

# write()
try:
    s = "asdasdasdasd!"
    file = 'test.txt'   
    file = renameFile(file)
    f = open(file, 'w')
    f.write(s) # IOError
except IOError as e:
    print(e)
    print('파일을 쓰는데 오류가 발생했습니다.')
finally:
    if f: f.close()

# with ~ as 구문 (close() 자동으로 호출)
try:
    s = "asdasdasdasd!"
    file = 'test.txt'   
    file = renameFile(file)
    
    with open(file, 'w') as f: 
        f.write(s) # IOError
except IOError as e:
    print(e)
    print('파일을 쓰는데 오류가 발생했습니다.')
finally:
    print(f.closed) # False
    if f: f.close()


# read()
try:
    f = open('test.txt', 'r') # FileNotFoundError
    s = f.read() 
    print(s)
except FileNotFoundError as e:
    print("존재하는 파일이 없습니다.")
except IOError as e:
    print("파일을 읽는데 오류가 발생했습니다.")
finally:
    if f: f.close()

# with ~ as 구문 (close() 자동으로 호출)
try:
    with open('test.txt', 'r') as f:
        s = f.read()
        print(s)
except FileNotFoundError as e:
    print("존재하는 파일이 없습니다.")
except IOError as e:
    print("파일을 읽는데 오류가 발생했습니다.")
finally:
    print(f.closed)
    if f: f.close()

"""
read(): 파일 전체 다 읽음
readline(): 한 번에 한 줄씩 읽음
readlines(): 파일 전체를 라인 단위로 읽어서 리스트에 저장

write(): 파일에 한번에 출력
writelines(): 리스트 안에 있는 각 문자열을 파일로 출력
"""

s = "adasdadasdasdasdsadasd\n\
adasdasdasdasdasdasd\n\
asdasdadasdadasdasd"

s = """adasdadasdasdasdsadasd
adasdasdasdasdasdasd
asdasdadasdadasdasd"""

with open('test.txt', 'w') as f:
    f.write(s)

with open('test.txt', 'r') as f:
    s = f.read()
    print(s)

with open('test.txt', 'r') as f:
    while True:
        s = f.readline() # enter까지 읽음 (대용량 파일에서는 한 줄씩 읽는 게 좋음)
        print(s, end='')
        if(not s): break

with open('test.txt', 'r') as f:
    s = f.readlines() 
    # enter까지 읽음 (대용량 파일에서는 한 줄씩 읽는 게 좋음)
    # 라인 단위로 리스트에 저장
    print(s)

with open('test_copy.txt', 'w') as f:
    f.writelines(s) # 리스트에 들어간 라인 단위의 문자열을 파일에 출력


#############################################################
import pickle
# 객체를 파일로 저장하고 싶을 때
# 저장 모드: 이진 파일 (wb, rb)

with open('pickle.txt', 'wb') as f:  
    #li = [1, 2, 3, 4, 5]
    dic = {'a':1, 'b':2, 'c':3}
    pickle.dump(dic, f) # pickling (파일 쓰기)

with open('pickle.txt', 'rb') as f:
    dic = pickle.load(f) # 파일 읽음
    print(dic)
    print(type(dic))

#############################################################
import json

with open('test.txt', 'w') as f:
    li = [1, 2, (3, 4), {'a':1, 'b':2, 'c':3}]
    s = json.dumps(li) # json stringify
    print(s)
    print(type(s)) # str
    f.write(s)

with open('test.txt', 'r') as f:
    s = f.read()
    li = json.loads(s) # json parsing
    print(li)
    print(type(li))