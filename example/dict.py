# Dictionary의 특징과 기본 사용법
var = {'name' : 'chris', 'age' : 23, 1 : ['a' , 'b', 'c']}
print(var)
print(var['name'])


var['age'] = 33
print(var)
del var[1]
print(var)
var[1] = 'Hi'
print(var)


var.update({'name' : 'hans', 'age' : 30})
print(var)


data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = {'3rd' : 'hans', '4th' : 'james', '5th' : 'jenny'}
var = {**data_1, **data_2}
print(var)
var = data_1 | data_2   # Python 3.9 이상에서만 사용 가능
print(var)


# 얕은 복사와 깊은 복사
data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = data_1
print(data_1)
print(data_2)
data_1['1st'] = 'hans'
print(data_1)
print(data_2)


data_1 = {'1st' : 'chris', '2nd' : 'tommy', '3rd' : 'harry'}
data_2 = data_1.copy()
print(data_1)
print(data_2)
data_1['1st'] = 'hans'
print(data_1)
print(data_2)


# Dictionary Comprehension의 특징과 예
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print(var)
var = { name : age for name, age in var.items() if age < 20}
print(var)


# Dictionary 관련 함수
# keys() : Dictionary의 key를 반환
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print(var.keys())


# values() : Dictionary의 value를 반환
print(var.values())


# items() : Dictionary의 key와 value를 반환
print(var.items())


# clear() : Dictionary의 모든 값을 제거
var.clear()
print(var)


# get() : Dictionary의 특정 key의 value를 반환
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
print('chris' in var)
print(var.get('chris'))
print('hans' in var)
print(var.get('hans'))
print(var.get('hans', 'hans is not in var'))


# Dictionary의 활용
# 다양한 루프 테크닉
var = {'chris' : 10, 'tommy' : 30, 'harry' : 20}
for k, v in var.items():
    print(k, v)


for i, v in enumerate(['chirs', 'tommy', 'harry']):
    print(i, v)
   
name = ['chris', 'tommy', 'harry']
age = [10, 30, 20]
for k, v in zip(name, age):
    print(k, v)
   
# Json과 Dictionary 변환
import json


var = '{"chris" : 10, "tommy" : 30, "harry" : 20}'
print(var)
print(type(var))


var = json.loads(var)
print(var)
print(type(var))


var = json.dumps(var)
print(var)
print(type(var))
