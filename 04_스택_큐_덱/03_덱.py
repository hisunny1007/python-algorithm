### 덱 deque
## collections에서 가져와야 함

from collections import deque

queue = deque()

# enqueue (앞, 뒤)
queue.appendleft(1)
queue.appendleft(2)
queue.append(3)
queue.append(4)
print(queue) # deque([2, 1, 3, 4])

# dequeue (앞, 뒤)
print(queue.popleft()) # 2
print(queue.pop()) # 4

# peek (앞, 뒤)
print(queue[0]) # 1
print(queue[-1]) # 3

# deque 덱은 시간에서 유리함
# but, deque가 무조건 빠른 건 아님!
# 덱이 효율성이 안 나는 상황은? => 가운데 조회할 때
# deque의 가운데에 있는 값을 조회할 때 불리


# deque은 양방향 연결 리스트
# 끝에 있는 값은 [-1]로 보면 되는데  (-1 인덱스) 
# 가운데 값은 앞에서부터 쭉 봐야하기 때문에 가장 효율이 안남

# 덱에서 조회는 O(N)
# 조회할 때는 불리함! 넣고 빼기만 할 때는 유리함!

# 큐 -> 덱
# 덱을 가지고 조회할 때 쓰면 시간초과남