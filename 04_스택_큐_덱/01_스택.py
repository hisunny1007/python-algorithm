### 스택 stack
## 파이썬에서는 리스트를 스택으로 사용

stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)    # [1, 2, 3]
# 머릿속으로는 아래에서 위로 생각하자
"""
3
2
1
"""

# pop
print(stack.pop())  # 3
print(stack.pop())  # 2

# peek
# 꺼내지않고 스택의 가장 맨 위에 있는 데이터 조회 (-1 인덱스 사용함)
print(stack[-1])    # 1