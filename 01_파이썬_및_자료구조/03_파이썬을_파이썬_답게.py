## 1. List Comprehension (리스트 컴프리헨션)
numbers1 = []  # [1, 2, 3, 4, 5]

for i in range(1, 6):
    numbers1.append(i)

print(numbers1)

# [ 원소 | 원소에 대한 반복문 ]
# * 헷갈린다면 빈 리스트 [] 만들고 for문 그대로 복사하고 append 안에 들어가는 거 왼쪽에다 넣어
numbers2 = [i for i in range(1, 6)]
print(numbers2)  # [1, 2, 3, 4, 5]

numbers3 = []
for i in range(1, 6):
    if i % 2 == 0:
        numbers3.append(i)
print(numbers3)

# [ 리스트에 들어갈 원소 | 원소에 대한 반복문 | 반복문에 대한 조건문]
numbers4 = [i for i in range(1, 6) if i % 2 == 0]
print(numbers4)  # [2, 4]


## 2. 다중 할당, 패킹, 언패킹
# 2-1. 다중 할당
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

a, b = b, a
print(a, b)  # 2 1

# 2-2. 패킹(Packing) -> 리스트로 감싼다
a, *b = 1, 2, 3, 4
print(a)  # 1
print(b)  # [2, 3, 4]

*a, b = 1, 2, 3, 4
print(a)  # [1, 2, 3]
print(b)  # 4

# 2-3. 언패킹(Unpacking) -> 감싼 걸 해제한다
# a, b, c = [1, 2, 3] 언패킹은 대괄호를 없애고 자릿수에 맞게 다중할당 해줌
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)  # 1 2 3


numbers = [1, 2, 3]

for number in numbers:
    print(number, end=" ")  # 1 2 3
print()

# * 연산자 : 할당할 때는 패킹 / 아닐 때는 언패킹
# * 언패킹은 대괄호 없애고 그대로 print에  들어감 / print는 여러 개 인자 넣으면 공백을 기준으로 출력
numbers = [1, 2, 3]
print(*numbers)  # print(1, 2, 3) ->  # 1 2 3


## 3. enumerate
numbers = [8, 2, 5, 3]
# 0번째 원소 : 8
# 1번째 원소 : 2
# ...

for i in range(len(numbers)):
    print(f"{i}번째 원소 : {numbers[i]}")

# enumerate(리스트)
# 리스트의 인덱스랑 원소를 담은 튜플이 생기고 얘를 하나하나 꺼내서 다중할당 해준다
for i, number in enumerate(numbers):
    print(f"{i}번째 원소 : {number}")
# enumerate에 리스트 넣으면
# enumerate(numbers) -> 튜플의 개념적 집합이 나옴 (인덱스, 원소)
# (0, 8)
# (1, 2)
# (2, 5)
# (3, 3)

# 파이썬스러운 문법을 잘 알면 이렇게 한 줄로 작성 가능
# [(0, 1, 2, 3), (8, 2, 5, 3)] [(인덱스), (원소)]
print(list(zip(*enumerate(numbers))))


## 4. Counter
# 4-1. 딕셔너리를 이용한 카운팅
numbers = [1, 2, 4, 1, 2, 2, 3, 2, 2]
# numbers의 원소가 각각 몇개 있는지 알고 싶다면?

counter = {}

for number in numbers:
    # 만약, 딕셔너리에 이미 있으면 -> + 1
    if number in counter:
        counter[number] += 1
    # 만약, 딕셔너리에 없으면 -> 1개로 넣어
    else:
        counter[number] = 1

# for number in numbers:
#     # number가 key값
#     # if counter.get(number):
#   if counter.get(number):
#     counter[number] += 1
#   else:
#     counter[number] = 1

print(counter)  # { 1: 2, 2: 5, 3: 1, 4: 1 }


# 4-2. 카운터 모듈을 이용한 카운팅
# 카운터 클래스 - 딕셔너리로 쓸 수 있음
from collections import Counter

numbers = [1, 2, 4, 1, 2, 2, 3, 2, 2]
counter = Counter(numbers)

print(counter)  # Counter({2: 5, 1: 2, 4: 1, 3: 1})

# collections 모듈 안에 있는 Counter 클래스임 / counter 객체의 most_common 메서드
common = counter.most_common()  # 가장 많이 나오는 순서대로 정렬
print(common)  # [(2, 5), (1, 2), (4, 1), (3, 1)]
print(common[0])  # (2, 5) 튜플 그 자체가 나옴
print(common[0][0])  # 2
