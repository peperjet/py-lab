#chapter03-5
#파이썬 딕셔너리
#범용적으로 가장 많이 사용
#딕셔너리 자료형 (순서X, 중복X, 수정O, 삭제O) - 가변

#선언
a = {'name':'Kim', 'phone':'01033337777', 'birth':'000101'}
b = {0:'Hello Python'}
c = {'arr':[1,2,3,4,5]}
d = {
    'name':'Niceman',
    'city':'Seoul',
    'age':33,
    'grade':'A',
    'status':True
}

e = dict([
    ('name','Niceman'),
    ('city','Seoul'),
    ('age',33),
    ('grade','A'), 
    ('status',True)
])


f=dict(
    name='Niceman',
    city='Seoul',
    age=33,
    grade='A',
    status=True
)


print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print() 


#출력
print('a - ', a['name']) #존재하지 않는 key 접근시 에러
print('a - ', a.get('name')) #존재하지 않는 key 접근시 None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('city'))
print('f - ', f.get('Age'))


#딕셔너리 추가
a['address'] = 'Seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

#딕셔너리 추가
print('a - ', len(a)) #key의 갯수
print('b - ', len(b))
print('b - ', len(c))
print('b - ', len(d))

#딕셔너리 keys(), values(), items() : 반복문에서(__iter__) 사용가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name')) 
print('a - ', a)
print('a - ', c.pop('arr'))
print('a - ', c)


print()
print('f - ', f.popitem()) #임의 삭제
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()


print('a - ', 'birth' in a) #key 존재 유무 확인
print('a - ', 'City' in d) #대소문자 구분

#수정
a['test'] = 'test_dict'

print('a - ', a)

a['address'] = 'dj'
print('a - ', a)


a.update(birth='910904')
print('a - ', a)
temp = {'address':'Busan'}

a.update(temp)
print('a - ', a)


print()

# 딕셔너리 10문제 

# 1.딕셔너리 {"a": 1, "b": 2}에서 key "a"의 값을 출력하라.
d = {"a": 1, "b": 2} 
print(d["a"])

# 2.딕셔너리 {"a": 1}에 "b": 2를 추가하여 출력하라.
d = {"a": 1}
d["b"] = 2
print(d)

# 3.딕셔너리 {"a": 1, "b": 2}에서 모든 key를 출력하라.
d = {"a": 1, "b": 2}
for key in d.keys():
    print(key)


# 4.딕셔너리 {"a": 1, "b": 2}에서 모든 value를 출력하라.
d = {"a": 1, "b": 2}
print(d.values())


# 5.딕셔너리 {"a": 1, "b": 2}에서 key "c"가 없으면 0을 출력하라.
d = {"a": 1, "b": 2}
print(d.get("c", 0))


# 6.딕셔너리 {"apple": 3, "banana": 5}에서 "apple"의 값을 10으로 변경하라.
d = {"apple": 3, "banana": 5}
d["apple"] = 10
print(d)


# 7.딕셔너리 {"a": 1, "b": 2}에서 key "b"를 삭제하라.
d = {"a": 1, "b": 2}
del d["b"]
print(d)


# 8.딕셔너리의 모든 key와 value를 한 줄씩 출력하라.
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(f"{key}: {value}")    



# 9.리스트 [("a", 1), ("b", 2)]를 딕셔너리로 변환하여 출력하라.
l = [("a", 1), ("b", 2)]
d = dict(l)
print(d)


# 10.딕셔너리 {"a": 1, "b": 2, "c": 3}에서 value의 합을 출력하라.
d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))
