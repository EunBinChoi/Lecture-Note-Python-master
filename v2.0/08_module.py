# 모듈 (module)
# 함수, 변수, 클래스를 묶어놓은 파일
# 1) 표준 모듈 (파이썬 내부 모듈)
# 2) 사용자 정의 모듈

# 이름 공간 (namespace)
# : 현재 함수, 변수, 클래스가 존재하는 장소
# : ex) 파일 이름 지역/전역

mypi = 3.141592
#import mymath
#print(mymath.mypi)
#print(mymath.area(2))
#print(mypi)

# import pandas as pd
# import numpy as np
import mymath as mm
print(mm.mypi)
print(mm.area(2))

#from mymath import area
#print(area(2)) # 모듈 이름 없이 사용 가능

#mypi = 3.141592
#from mymath import *
#print(mypi) # 모듈 이름 없이 사용 가능
#print(area(2)) # 모듈 이름 없이 사용 가능

##########################################

g = 10 # global
h = 5 # global

def f(a): # a: local
    global h # 함수 내에서 global한 변수를 사용하고 싶을 때
    h = a + 10 # global
    print(h)

f(2)
print(h) # 12
