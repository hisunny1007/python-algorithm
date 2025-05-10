# 백준 행렬 덧셈 https://www.acmicpc.net/problem/2738
# 오후 9시 49분 -> 9시 59분

## 방법 1.
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# a = []
# b = []

# for _ in range(n):
#     line = list(map(int, input().split()))
#     a.append(line)
# # print(a) # [[1, 1, 1], [2, 2, 2], [0, 1, 0]]


# for _ in range(n):
#     line = list(map(int, input().split()))
#     b.append(line)
# # print(b) # [[3, 3, 3], [4, 4, 4], [5, 5, 100]]

# for i in range(n):
#     for j in range(m):
#         answer = a[i][j] + b[i][j]
#         print(answer, end = " ") # 4 4 4 6 6 6 5 6 100
#     print()


## 방법 2.
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# matrix1 = []

# for _ in range(n):
#   line = list(map(int, input().split()))
#   matrix1.append(line)
# print(matrix1)

# 이걸 리스트 컴프리헨션으로
matrix1 = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(m):
    # matrix1에 수정하기
    matrix1[i][j] += matrix2[i][j]
# print(matrix1) # [[4, 4, 4], [6, 6, 6], [5, 6, 100]]

# for i in range(n):
#    for j in range(m):
#       print(matrix[i][j], end=" ")
#    print()

for line in matrix1:
    # print(line)
    '''
    [4, 4, 4]
    [6, 6, 6]
    [5, 6, 100]
    '''
    print(*line)


## 방법 3.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
   line = list(map(int, input().split()))
   for j in range(m):
      matrix[i][j] += line[j]

for i in range(n):
   print(*matrix[i])