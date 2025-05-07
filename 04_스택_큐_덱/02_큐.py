### 큐 queue
## 파이썬에서는 큐도 리스트로 구현

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue) # [1, 2, 3]

# dequeue
print(queue.pop(0)) # 1
print(queue.pop(0)) # 2

# peek
print(queue[0]) # 3


# pop(0) : 시간복잡도 O(N)
# 리스트(스택, 큐)의 데이터가 많을수록 많은 시간 소요

# 맨 앞에꺼 뺐으니까 나머지것들 앞으로 하나씩 당겨줘야 함
# n개를 앞으로 당겨주느라
# => 덱(deque)쓰면 빠름

# 덱 deque (double ended queue) : 시간복잡도 O(1)
# 양쪽으로 넣고 뺄 수 있는 양방향 연결리스트
# 나머지 애들 밀 필요 없이 제거만 하면 되니까
# appendleft() popleft() append() pop() => 시간복잡도는 모두 O(1)

# => 큐 문제 나오면 무조건 덱으로 푼다!