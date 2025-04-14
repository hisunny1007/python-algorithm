# print
print("1")

## 1. 여러 인자를 넣으면 공백을 기준으로 출력
print("1", "2", "3")  # 1 2 3
# print("1", "2", "3", sep=" ") # 기본 값


## 2. 맨 끝의 개행을 다른 문자로 바꿀 수 있다. (end)
print("hello", end="$")  # hello$
print("python")  # hello$python 개행안하고 $ 로 바꿨으니까 이렇게 나옴
# print("python", end="\n") # end="\n" 생략되어있음 (print 자체가 기본값이 개행으로 되어있음)


## 3. 구분자를 다른 문자로 바꿀 수 있다. (sep)
print("1", "2", "3", sep="$")  # 1$2$3
print("1", "2", "3", sep="\n")  # 자주 쓰이는 것! (한 줄씩 출력)
# 1
# 2
# 3


## 4. f-string (문자열 포매팅)
name = "sunny"
print("안녕하세요! " + name)  # 안녕하세요! sunny
print(f"안녕하세요! {name}")  # 안녕하세요! sunny

age = 40
print(
    f"안녕하세요! {name}, 나이는 {age - 20}입니다."
)  # 안녕하세요! sunny, 나이는 20입니다.


## 5. A + B - 7
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    # 공백을 기준으로 잘라야지. 근데 문자열이니까 map을 씌워서 int를 먹여야지
    a, b = map(int, input().split())
    print(f"Case #{i + 1}: {a + b}")  # Case #1: 2

# for i in range(1, t+1):
#   a, b = map(int, input().split())
#   print(f"Case #{i}: {a + b}")


## 6. A+B - 8
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(f"Case #{i + 1}: {a} + {b} = {a + b}")
