### 컨테이너 자료형

## 1. 순서가 있는 자료형 vs 순서가 없는 자료형
## 2. 변경 가능한 자료형 vs 변경 불가능한 자료형

## 3. 할당 vs 얕은 복사 vs 깊은 복사
# 3-1. 할당
a = [1, 2, 3] # a는 [1, 2, 3]의 주소값을 가리킴
b = a # b는 a 자체가 아닌 a가 가리키고 있는 것을 가리킴

print(a) # [1, 2, 3]
print(b) # [1, 2, 3]

b[0] = 4
print(a) # [4, 2, 3]
print(b) # [4, 2, 3]

# 할당하면 같이 바뀌니까 얕은 복사하는 게 좋음

a = "hello"
b = a       # 할당
print(a)    # hello
print(b)    # hello

b += "!"
print(a)    # hello
print(b)    # hello!
# ⇒ mutable과 immutable의 차이


# 3-2. 얕은 복사
from copy import copy

a = [1, 2, 3]
b = a[:] # 복제 1
b = list(a) # 복제 2
b = copy(a) # 복제 3

b[0] = 4
print(a) # [1,2,3]
print(b) # [4,2,3]


# 3-3. 깊은복사(deepcopy)
# 얕은 복사의 한계 때문에 필요
a = [[1,2,3], [4,5,6]]
b = a[:] # 얕은 복사함

b[0][0] = 9
print(a) # [[9,2,3], [4,5,6]]
print(b) # [[9,2,3], [4,5,6]]
# 얕은 복사는 겉에꺼 하나만 복사하기 때문에 안에 있는 건 여전히 동일


# 이중for문으로 복사해도 되고
# deepcopy 써도 됨 (3차원 리스트도 다 해주기때문에 더 편함)
from copy import deepcopy
a = [[1,2,3], [4,5,6]]
b = deepcopy(a)

b[0][0] = 9
print(a) # [[1,2,3], [4,5,6]]
print(b) # [[9,2,3], [4,5,6]]
