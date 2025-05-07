### 이차원 리스트 순회

## 1. 행 우선 순회 (행순회) ⇨
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

"""
다음과 같이 출력하여라
1 2 3 4
5 6 7 8
9 0 1 2
"""

# print(matrix) # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

# 행에 대한 반복 -> 하나의 행 안에서도 열로 반복해야 함 => 이중 for문
for i in range(3):  # 행
    for j in range(4):  # 열
        # print(matrix[i][j]) # print는 기본적으로 한 줄 내림
        # 1
        # 2
        # ..
        # 2
        print(matrix[i][j], end=" ") # 1 2 3 4 5 6 7 8 9 0 1 2

    print()  # 한 행을 출력 후 개행하기 위함 (들여쓰기 중요함!)

    # 이거 자체가 한 행을 의미함
    # for j in range(4):
    #     print(matrix[i][j], end = " ")


## 2. 열 우선 순회 (열순회) ⇩
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

"""
다음과 같이 출력하여라
1 5 9
2 6 0
3 7 1
4 8 2
"""

for i in range(4):  # 열
    for j in range(3):  # 행
        print(matrix[j][i], end=" ")
    print()

        # 인덱스 초과했다고 에러남 (행-열로 해야됨)
        # print(matrix[i][j], end = " ")

# 결론 (열순회)
# 열이 바깥 for문이 되어야 함
# 안에서 matrix로 조회할 때 열과 행을 스위치해서 조회해야지만 에러가 나지 않는다


## 3. 이차원 리스트의 총합
matrix = [
    [0, 5, 3, 1],
    [4, 6, 10, 8],
    [9, -1, 1, 5]
]

total = 0

# 행순회 이용
for i in range(3): # 행
    for j in range(4): # 열
        total += matrix[i][j]

print(total)    # 51

    # 이거 자체가 한줄, 즉 일차원 리스트임
    # for j in range(4): 
    #     total += matrix[i][j]


# 파이썬 내장함수 sum(컨테이너)
# 컨테이너에는 리스트도 들어감
# => 내장함수 sum 이용 가능

# 내장함수 sum 이용 가능
total = 0

# for i in range(3):
#     total += sum(matrix[i])
# for문 개수만으로는 시간복잡도 알 수 없음
# => sum 자체가 리스트를 순회함
# => 위랑 동일한 시간복잡도 가짐 ON(제곱)

for line in matrix:
    total += sum(line)

print(total)    # 51