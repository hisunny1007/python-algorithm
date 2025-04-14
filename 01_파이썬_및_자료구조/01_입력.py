### input, readline
## 1. input을 이용한 기본 문법
n = int(input())
print(n)


## 2. readline을 이용한 빠른 입력
import sys

# 괄호쓰면 결과 할당하는건데 이거는 함수 자체를 할당하는것. readline을 인풋이란 이름으로 쓸 거야
input = sys.stdin.readline

n = int(input())
print(n)

# 문자열을 list로 바꿔줌
word = list(input())
print(word) # ['h', 'e','l','l','o','\n']


# rstrip() 공백이나 개행 없애줌
# 문자열로 받을 때는  rstrip 꼭 필요함 (숫자는 자동으로 해줘)
word = list(input().rstrip())
print(word) # ['h', 'e','l','l','o']


## 3. 한 줄 리스트 입력
import sys

input = sys.stdin.readline

# numbers = map(int, input())
# print(numbers) <map object at 0x00000245B5FE4400> map이라고만 쓰면 주소값만 나옴! list 붙여줘야 함

numbers = list(map(int, input().split()))
print(numbers)

# input().split()
# .split() 공백을 기준으로 문자열 리스트로 나눔
# "1 2" -> ["1", "2"]

# map(int, input().split())
# map(함수, 컬렉션) 첫번째 인자는 함수 자체, 이 함수가 오른쪽의 컬렉션에 하나하나 적용된다는 것 (각각의 함수를 원소에 매핑한다)
# map(int, ["1", "2"]) -> int("1") int("2") -> 1 2

# list(map(int, input().split())) 마지막에 리스트로 바꿔줌
# 1 2 -> [1 2]

# 다중 할당도 가능
a, b = list(map(int, input().split()))
print(a + b)

# 다중할당으로 받을 때는 list로 감싸지 않아도 됨
a, b = map(int, input().split())

# list외에도 다른 collection으로 처리 가능
numbers = tuple(map(int, input().split()))
numbers = set(map(int, input().split()))


## 4. A+B -2
import sys

input = sys.stdin.readline

# input은 한 줄만 받음
a = int(input())
b = int(input())
print(a + b)


## 5. A+B -3
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())  # .split 문자열을 공백으로 나눠서 map 각각의 원소에 int 먹이고 다중할당해줌
    print(a + b)

## 6. A+B - 6
import sys

input = sys.stdin.readline

t = int(input())

# split 기본적으로 구분자는 공백, 개행임
# split 안에 구분자를 직접 추가할 수 있음 ","

for _ in range(t):
  a, b = map(int, input().split(","))
  print(a + b)

