### 논리 연산자

## and(&&), or(||), not(!)
# and 정확한 수행 로직
# 좌항이 False(0, "", ...)인 값이면 좌항을 반환
# 좌항이 True인 값이면 우항을 반환
print(True and True)    # True
print(1 and 1)          # 1
print(0 and 1)          # 0

# or 정확한 수행 로직
# 좌항이 True인 값이면 좌항을 반환
# 좌항이 False인 값이면 우항을 반환
print(True or False)    # True
print(0 or -1)          # -1
print("" or True)       # True
print(0.0 or 10.0)      # 10.0

## 우선 순위
# 비교 연산자와 논리 연산자를 함께 사용하면 비교 연산자 먼저 실행됨
