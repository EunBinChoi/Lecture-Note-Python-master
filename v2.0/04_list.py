# li sort(), sorted(), reverse(), reversed()

# li.sort(), li.reverse(): li 자체를 변경
# changed = sorted(li), changed = reversed(li):
# : li는 수정하지 않고 새로운 리스트로 반환 

li = [30, 50, 0, -100, -200, -1000]
li.sort() # 오름차순 정렬
print(li)
print()

li = [30, 50, 0, -100, -200, -1000]
changed = sorted(li) # 오름차순 정렬
print(li)
print(changed)
print()

li = [30, 50, 0, -100, -200, -1000]
li.reverse()
print(li)
print()

li = [30, 50, 0, -100, -200, -1000]
changed = reversed(li)
print(li)
print(list(changed))
print()

# Q1. 내림차순 정렬
li = [30, 50, 0, -100, -200, -1000]
li = sorted(li)[::-1]
print(li)

# Q2. 정렬해야하는 대상
li = [('lee', 30), ('park', 60), ('ahn', 100)]
li.sort() # 튜플 중에서 이름순 정렬
print(li)

def comp(tu):
    return tu[1]
    
#comp = lambda tu : tu[1]

li.sort(key=lambda tu : tu[1]) # 튜플 중에서 나이순 정렬
print(li)


# Q3. 리스트의 원소를 숫자로 가정하여 숫자 정렬
li = ['123', '34', '56', '2345']
# li = ['34', '56', '123', '2345']

li.sort()
print(li)

li.sort(key=lambda element : int(element))
print(li)

# Q4. list comprehension을 이용하여 피타고라스를 만족하는 세 변의 길이 쌍
# 1) x ** 2 + y ** 2 == z ** 2
# 2) x + y > z (삼각형 성립조건)
# 3) x <= y <= z
# 4) 1 <= x, y, z <= 100

# [(3, 4, 5), ......]

li = [(x, y, z) for x in range(1, 101) for y in range(1, 101) for z in range(1, 101) 
                if x**2 + y**2 == z**2 and x + y > z and x <= y <= z]
print(li)
print(len(li))