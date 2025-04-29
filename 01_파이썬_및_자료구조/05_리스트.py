### 리스트

## 1. append
numbers = [1, 2, 3]
numbers.append(4)
print(numbers) # [1, 2, 3, 4]
# => append(4) 원소 하나 추가하면 시간복잡도는 O(1)


## 2. pop
# 가장 끝에 있는 원소 제거하고 반환함
# pop() 마지막꺼만 하면 시간복잡도는 O(1)
numbers = [1, 2, 3]
number = numbers.pop()
print(numbers) # [1, 2]
print(number) # 3
# => pop() 마지막꺼만 하면 시간복잡도는 O(1)

# 어디서 빼냐에 따라 시간복잡도 달라진다
numbers = [1, 2, 3]
number = numbers.pop(0)
print(numbers) # [2, 3]
print(number) # 1
# => 앞이나 중간에서 빼면 다 뒤로 밀리니까 시간복잡도는 O(N) 


## 3. count
numbers = [1, 2, 2, 3]
counts = numbers.count(2)
print(counts) # 2
# => count는 내부에서 알아서 for문 돌아서 찾는 거라 시간복잡도는 O(N)


## 4. sort
# 변경 가능한 자료형이니까 원본이 바뀜!!!
numbers = [4, -1, 0, 2, 100]
numbers.sort() # 기본 오름차순 정렬
print(numbers) # [-1, 0, 2, 4, 100]
# => 시간복잡도는 O(NlogN)

numbers.sort(reverse=True) # 내림차순 정렬
print(numbers) # [100, 4, 2, 0, -1]
# => 시간복잡도는 O(NlogN)