import sympy as sp
import random
import numpy as np #넘파이 행렬 계산을 빠르게 해준다

# 예제 1. 합, 스칼라배 활용 예제
A = sp.Matrix([[1, 2, -4],
               [-2, 1, 3]])

B = sp.Matrix([[0, 1, 4],
               [-1, 3, 1]])

C = sp.Matrix([[1, 1],
               [2, 2]])

# A + B : 같은 위치 숫리끼리 더함
print("A + B =")
print(A + B)
print()

# 2A : 모든 숫자에 2를 곱함
print("2A =")
print(2*A)
print()

# (-1)C : 모든 숫자에 -1을 곱함
print("(-1)C =")
print((-1)*C)



# 예제2. 행렬의 곱 활용
A2 = sp.Matrix([[1, 2, -1],
                [3, 1, 0],])
B2 = sp.Matrix([[-2, 1],
                [0, -3],
                [2, 1]])

# 행렬 곱
print("A2 * B2 =")
print(A2 * B2)


# 예제3 전치행렬
A3 = sp.Matrix([[1, -2, 3],
                [4, 5, 0],])
B3 = sp.Matrix([[1, 2, -4],
                [3, -1, 2],
                [0, 5, 3]])
C3 = sp.Matrix([[5, 4],
                [-3,2],
                [2, 1]])
D3 = sp.Matrix([[3, 0, 1]])

print("A3^T =")
print(A3.T)
print()

print("B3^T =")
print(B3.T)
print()

print("C3^T =")
print(C3.T)
print()

print("D3^T =")
print(D3.T)
# 전치행렬 : 행 ↔ 열 위치만 뒤집는 것.


# 예제4 SageMath Cell 서버에서 임의로 행렬을 하나 생성하고, 그 행렬의 전치행렬 구하기
A4 = sp.Matrix([[random.randint(-10,10) for j in range(12)] for i in range(7)])

print("A4 =")
print(A4)
print()

print("A4^T =")
print(A4.transpose())


# 예제5 넘파이
A5 = np.array([
[1,1,2],
[2,4,-3],
[3,6,-5]
])

print(A5)



# 예제6 : 임의의 5x7 행렬 생성
A6 = np.random.randint(5, size=(5,7)) # 0~4 사이의 정수로 5행 7열의 행렬 생성

print("A6 =")
print(A6)
print()

print("A6^T =")
print(A6.transpose()) #전치행렬 7x5