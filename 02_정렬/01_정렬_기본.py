### 정렬

## 오름차순 정렬
# 내장함수 sorted() 이용 / 리스트 메서드 .sort() 이용
# 둘 다 시간 복잡도는 O(nlogn)

# 내장함수 sorted()는 원본은 변경하지 않고 새롭게 정렬된 리스트를 반환함
# 리스트 메서드 .sort()는 원본을 변경함(그래서 할당하지 않음)

numbers = [1, 3, -4, 0, 100]

sorted_numbers = sorted(numbers)
# sorted(numbers)는 내장 함수여서 이 자체가 정렬된 리스트 반환함

print(numbers)  # [1, 3, -4, 0, 100]
print(sorted_numbers)  # [-4, 0, 1, 3, 100]
# => 원본은 변경되지 않고 정렬된 리스트 반환
# sorted는 내장함수임! 내장함수는 특정 자료형에 소속돼있는 게 아니라 범용적으로 사용 가능함
# 다른 컨테이너 자료형 모두 가능 (리스트뿐만 아니라 정렬될 수 있는 자료형)
# 리스트가 아닌 정렬 가능한 다른 자료형(set, tuple, ...)도 가능


numbers = [1, 3, -4, 0, 100]

numbers.sort()
print(numbers)  # [-4, 0, 1, 3, 100]
# ⇒ 원본 리스트가 변경
# 파이썬 리스트는 mutable 변경 가능한 자료형이기 때문
# .sort() 리스트에 소속된 메서드여서 리스트에만 적용됨


## 내림차순 정렬
# reverse 조건만 추가하면 끝
numbers = [1, 3, -4, 0, 100]

sorted_numbers = sorted(numbers, reverse=True)

print(numbers)  # [1, 3, -4, 0, 100]
print(sorted_numbers)  # [100, 3, 1, 0, -4]

numbers = [1, 3, -4, 0, 100]

numbers.sort(reverse=True)
print(numbers)  # [100, 3, 1, 0, -4]