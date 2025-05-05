### 커스텀 정렬
# 내가 원하는 기준으로 정렬

## 1. 기본적인 방법을 이용한 커스텀 정렬
# 기본 문자열 정렬
words = ["hello", "abc", "z"]

print(sorted(words))  # ['abc', 'hello', 'z']
# 문자열은 기본적으로 사전순 정렬
# ⇒ 첫글자부터 abc 순으로 정렬됨


# 길이순으로 정렬하고 싶다면?
# 오름차순 정렬
def length(word):
    return len(word)


# sorted()는 key라는 옵션 쓸 수 있음(reverse옵션 말고)
# key 내가 원하는 기준 / key= 함수명
# key=함수명 / 함수를 직접 위에다 선언해 줘야됨
# 커스텀 정렬 하고 싶으면 그 기준을 key옵션에다 넣어! 근데 함수로써 부여해야 돼! 그 함수의 로직이 기준이 됨!
sorted_words = sorted(words, key=length)
# => len(word)를 기준으로 정렬하는 것
print(sorted_words)  # ['z', 'abc', 'hello']

# words.sort(key=length)


## 2. 리스트를 원소로 갖는 리스트(2차원 리스트) 커스텀 정렬
numbers = [[1, 13], [2, 7], [1, 7], [5, 10], [4, 20]]

print(sorted(numbers)) # [[1, 7], [1, 13], [2, 7], [4, 20], [5, 10]]
# ⇒ key를 지정하지 않으면 기본적으로 각 리스트의 첫번째 원소 기준으로 오름차순 정렬
# => 만약 첫 번째 요소가 같으면 두 번째 요소를 기준으로 오름차순 정렬 [[1, 7], [1, 13]]


# 첫 번째 원소를 기준으로 정렬하고 싶다면?
# 오름차순 정렬
def sort_key(unit): # unit에는 [1,13] [2, 7] 이렇게 리스트가 들어옴
    return unit[0]

sorted_numbers = sorted(numbers, key=sort_key)
print(sorted_numbers) # [[1, 13], [1, 7], [2, 7], [4, 20], [5, 10]]
# => sort_key 함수가 unit[0]을 반환하므로, 첫 번째 원소 기준으로 정렬
# => 다만, 첫 번째 값이 같은 경우에는 입력 순서 유지 (안정 정렬)

# sorted(numbers) => 첫 번째 원소 기준 + 같은 값일 땐 두 번째 값 기준
# sorted(numbers, key=sort_key) => 첫 번째 원소 기준, 같은 값일 경우 순서 유지


# 두 번째 원소를 기준으로 정렬하고 싶다면?
# 오름차순 정렬
def sort_key(unit):
    return unit[1]

sorted_numbers = sorted(numbers, key=sort_key)
print(sorted_numbers)  # [[2, 7], [1, 7], [5, 10], [1, 13], [4, 20]]
# [2, 7], [1, 7] 순서인 이유 : 7으로 기준이 같을 경우에는 원본 리스트의 순서를 보장함


# 두 번째 원소를 기준으로,
# 만약 두 번째 원소가 같다면, 첫 번째 원소를 기준으로 정렬하고 싶다면?
# 오름차순 정렬
def sort_key(unit):
    return unit[1], unit[0]  # 콤마로 여러 기준 쓸 수 있음

sorted_numbers = sorted(numbers, key=sort_key)
print(sorted_numbers)  # [[1, 7], [2, 7], [5, 10], [1, 13], [4, 20]]


## 3. Lambda 함수 활용하기
# 두 줄로 쓰기 싫어서 한 줄로 간편하게 쓸 수 있음 (리턴값만 있는 경우)
# 리턴값 외에 추가적인 로직 (if문, for문, ...) 있으면 람다로 못 씀!

# "lambda 매개변수: 리턴값"
# 매개변수 여러 개도 가능 / 리턴값은 한 개만 가능(튜플로 묶어줘야 함)

# 방법 1
def sort_key(unit):
    return unit[1]

# 방법 2 (방법 1과 동일함)
sort_key = lambda unit: unit[1]
# lambda unit: unit[1] 자체가 함수고 sort_key란 변수에 할당한 것임

print(sort_key([1, 2]))  # 2
# 변수에 할당했으니까 sort_key 자체를 함수명으로 호출할 수 있음


# 매개변수 여러 개 가능
# def sort_key(unit1, unit2):
#     return unit1[1]

# sort_key = lambda unit1, unit2: unit1[1]

# 리턴값 한 개만 가능 => 튜플로 묶어줘

# (동일 로직 1)
# def sort_key(unit):
#     return unit[1], unit[0]

# sorted_numbers = sorted(numbers, key=sort_key)
# print(sorted_numbers)

# (동일 로직 2)
# sort_key = lambda unit: (unit[1], unit[0])
# sorted_numbers = sorted(numbers, key=sort_key)
# print(sorted_numbers)

# (동일 로직 3)
sorted_numbers = sorted(numbers, key=lambda unit: (unit[1], unit[0]))
print(sorted_numbers)


# 단어의 길이로 정렬
words = ["hello", "abc", "z"]

def length(word):
    return len(word)

sorted_words = sorted(words, key=length)
print(sorted_words)  # ['z', 'abc', 'hello']

sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)  # ['z', 'abc', 'hello']

# len은 파이썬의 내장 함수
# 원래는 def len() 이런 거였음!
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['z', 'abc', 'hello']


## 절대값 정렬
# https://dailyalgo.kr/ko/problems/78


# 1. 기본적인 방법
def solution(numbers):
    def absolute(number):
        if number < 0:
            number = -number
        return number

        # 파이썬의 삼항 연산자
        # return -number if number < 0 else number

    result = sorted(numbers, key=absolute)

    return result


# 2. 람다식 이용하기
def solution(numbers):
    result = sorted(numbers, key=lambda number: -number if number < 0 else number)
    return result


# 3. 내장함수 abs 이용하기
def solution(numbers):
    result = sorted(numbers, key=abs)
    return result