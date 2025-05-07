### 이차원 리스트 입력

## 1. 행과 열이 미리 주어지는 경우
# 3 x 3
"""
1 2 3
4 5 6
7 8 9
"""
matrix = []

for _ in range(3): # 행의 개수만큼 반복
    line = list(map(int, input().split()))
    matrix.append(line)

print(matrix)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 리스트 컴프리헨션 사용 (위와 동일함)
matrix = [list(map(int, input().split())) for _ in range(3)]

print(matrix)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


## 2. 행과 열의 크기가 입력으로 주어지는 경우 (행==열)
# 3 x 3
"""
3
1 2 3
4 5 6
7 8 9
"""
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(matrix)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


## 3. 행과 열의 크기가 입력으로 주어지는 경우 (행!=열)
# 3 x 4
"""
3 4
1 2 3 4
5 6 7 8
9 0 1 2
"""
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(matrix)   # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]