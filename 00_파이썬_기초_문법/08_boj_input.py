### 백준 입출력

# split()은 문자열 메서드

# 입력
# 1
# 입력 코드
n = int(input())

# 입력
# "a"
# 입력 코드
c = input()

# 입력
# "spring flower"
# 입력 코드
a, b = input().split()

# 입력
# "spring flower warm"
# 입력 코드
a, b, c = input().split()

# 입력
# "1 2"
# 입력 코드
# (X) int(input().split()) // split의 반환값은 리스트임.
# split()은 list 자료형 반환
# => list 자료형은 int() 함수 적용 불가
# [1] -> 숫자 모양 X
# 리스트에 저장된 값 하나하나에 int() 함수 적용해야 함

# map이 메서드 아니고 함수임. 자바스크립트에서는 .map이었잖아
# map(리스트에 저장된 값에 적용할 함수, 리스트)
map(int, input().split())
n1, n2 = map(int, input().split())
print(n1, n2)   # 1, 2


# 2차원 리스트의 입력
# 입력
# 2(세로) 3(가로)
# 1 2 3
# 4 5 6
# 입력 코드
n, m = map(int, input().split())
list_2d = []
for i in range(n):  # for i in range(0, n, 1):
    list_1d = list(map(int, input().split()))  # [1, 2, 3]
    list_2d.append(list_1d)
print(list_2d)  # [[1, 2, 3], [4, 5, 6]]

# 파이썬은 굳이 m 활용하지 않음..
