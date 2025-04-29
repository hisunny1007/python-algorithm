### 문자열

## 1. join (무조건 문자열 원소들만 가능)
numbers = ["h", "e", "l", "l"]
joined_numbers = "".join(numbers) # 빈 문자열을 사이사이에다 넣어서 합쳐줘
print(joined_numbers) # hell

numbers = ["h", "e", "l", "l"]
joined_numbers = "$".join(numbers)
print(joined_numbers) #h$e$l$l

numbers = ["h", "e", "l", "l"]
print("\n".join(numbers)) # 하나씩 줄 바꿔서 나옴
"""
h
e
l
l
"""


## 2. replace(old, new)
word = "hello python"
new_word = word.replace("python", "java")
print(word)  # hello python
print(new_word)  # hello java
# 문자열은 원본 변경 불가능!!
# 원본을 바꿔주는 함수가 아니라 바꾼 문자열을 반환
# replace는 안 바뀜


## 3. 슬라이싱 string[start:end:step]
# step을 - 하면 방향이 반대로 바뀜
word = "hello"
print(word[1:3]) # el
print(word[0:4:2]) # hl
print(word[3:1:-1]) # ll
print(word[::-1]) # olleh (뒤집기)

def solution(n):
    answer = []
    
    for i in range(n-1, n):
        answer.append(i+1)
        
    return answer

# 프로그래머스 자연수 뒤집어 배열로 만들기 https://school.programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = []
    
    while n >= 1: # 한자리수가 남을 때까지만 반복
        #몫은 다음숫자, 나머지가 원소로 들어감
        answer.append(n % 10)
        n //= 10
        
    return answer # [5, 4, 3, 2, 1]

def solution(n):
    answer = []
    string_n = str(n) # 12345 -> "12345"
    numbers = list(map(int, string_n)) # "12345" -> [1, 2, 3, 4, 5]
    
    return numbers[::-1] # [5, 4, 3, 2, 1]