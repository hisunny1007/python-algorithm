### 딕셔너리

## 1. get
users = {"kyle": 20, "alex": 30, "jun": 40}
print(users["kyle"]) # 20
print(users.get("kyle")) # 20

# 키가 존재하지 않는 경우 (없는 키 값에 접근 시)
# [] => 에러 / .get => None

# print(users["justin"]) # key error 발생
print(users.get("justin")) # None
# => key가 존재하지 않는 경우에 대한 처리가 다름


# justin이 있으면 그의 숫자를 출력하고, 없으면 0을 출력
if "justin" in users:
  print(users["justin"])
else:
  print(0)

# 만약 justin이란 키가 없으면 2번째 인자로 적은 값 0을 출력함
print(users.get("justin", 0)) # 0


## 2. keys, values, items
users = {"kyle": 20, "alex": 30, "jun": 40}

for name in users.keys():
  print(name)
  """
  kyle
  alex
  jun
  """

for name in users:
  print(name)
  """
  kyle
  alex
  jun
  """

for value in users.values():
  print(value)
  """
  20
  30
  40
  """

for name, value in users.items():
  print(name, value)
  """
  kyle 20
  alex 30
  jun 40
  """

for name in users:
  print(name, users[name])
  """
  kyle 20
  alex 30
  jun 40
  """