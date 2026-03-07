# 260110 Chapter05-2
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입 (str)

# 예제 1 \n을 넣어 입력 칸을 다음줄로 넘겨주면 훨씬 명확하다.
# name = input("Enter Your Name : ") 
# grade = input("Enter Your Grade : ") 
# company = input ("Enter Your Company name : ")

# print(name, grade, company)
# print("_" *30)
# print(f"입력확인: {name}, {grade}, {company}")

# 예제 2
# number = input("Enter number : ")
# name = input("Enter name")

# print("type of number", type(number), number * 3)
# print("type of name", type(name))


# 예제 3
# first_number = int(input("Enter number1 : "))
# second_number = int(input("Enter number2 : "))

# total = first_number + second_number
# print("first_number + second_number : ", total)


# 예제 4
float_number = float(input("Enter a float number : "))

print("input float : ", float_number)
print("input type : ", type(float_number))


# 예제 5
print("FirstName - {0}, LastName - {1}".format(
    input ("Enter first name : "), 
    input("Enter second name") # 끝에 : 와 공백 추가
))