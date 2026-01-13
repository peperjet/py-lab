#파이썬 문자형
#문자형 중요


#문자열 생성
str1="I am Python"
str2='Python'
str3="""How are you?"""
str4='''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

#빈 문자열
str1_t1=''
str2_t2=str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

#이스케이프 문자 사용
#I'm boy

print("I'm boy")
print('I\'m boy')

print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

#탭, 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line\n Check!"

print(t_s1)
print(t_s2)
print()

#Raw String
raw_s = r'D:\python\test'
print(raw_s)
print()

#멀티라인 입력
multi_str = \
'''
String
Multi line
Test
'''
print(multi_str)
#문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3="How are you doing"
str_o4="Seoul Deagu Busan Incheon"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)
#대소문자 구분

#문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))


#문자열 함수 (upper, isalnum, startswith, count, etc...)
#첫글자 대문자
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("s"))

#260105
print("replace: ", str_o3.replace("doing", "going"))
print("sorted", sorted(str_o1))
print("split: ", str_o4.split("!"))

