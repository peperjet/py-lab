import pandas as pd
import numpy as np
import sympy as sp
import math

# 예제 1.
# 52장의 포커카드에서 5장의 카드를 뽑는 경우의 수 구하기 * 
# 카드에서 순서를 고려하지 않고 5 장을 뽑는 문제이다.

n = 52
r = 5

result = math.comb(n, r)

df = pd.DataFrame({
    'n': [n], 
    'r': [r], 
    'result': [result]
})

print(df)

# 더 간단한 방법 : math.comb() 함수를 사용하여 조합의 경우의 수를 계산할 수 있다.
print(math.comb(52, 5))
# 터미널 VS code에서는 print() 함수로 결과를 출력할 수 있다.



# 예제 2. 
# 500개의 전구로부터 5개의 백열전구를 택하는 방법의 개수는 5분의 500 = 5! 495!분의 500!이다.
n2 = 500
r2 = 5

result2 = math.comb(n2, r2)
print(result2)

# 더 간단한 방법
print(math.comb(500, 5))



# 예제  3 베이즈 정리 
# 공장에 기계 A, B, C가 있다.
# 생산 비율
# A : 전체 제품의 50%
# B : 전체 제품의 30%
# C : 전체 제품의 20%

# 각 기계의 불량률
# A : 4%
# B : 3%
# C : 2%

# 문제
# 1. 임의로 제품 하나를 뽑았을 때 불량일 확률을 구하라
# 2. 불량 제품이 나왔을 때 그것이 기계 C에서 생산됐을 확률을 구하라

P_A = 0.5
P_B = 0.3
P_C = 0.2

P_D_A = 0.04
P_D_B = 0.03
P_D_C = 0.02

# 전체 불량 확률 계산
P_D = P_A*P_D_A + P_B*P_D_B + P_C*P_D_C

# 불량 제품이 C 기계에서 생산됐을 확률
P_C_D = (P_C*P_D_C) / P_D

print(P_D)
print(P_C_D)
# 세 기계의 생산비율과 불량률을 이용해 전체 불량 확률과
# 불량이 C기계에서 나왔을 확률을 구하는 베이즈 정리 문제


# 예제 4. 
# 다음 확률분포에서 기댓값, 분산, 표준편차를 구하시오.
#
# x는 사건이 발생한 횟수이고 P(x)는 그 횟수가 나올 확률이다.
#
# x      : 0     1      2      3
# P(x)   : 0.010 0.840  0.145  0.005
#
# 목표
# 1. 기댓값(평균) 계산
# 2. 분산 계산
# 3. 표준편차 계산

# pandas DataFrame으로 확률분포를 표현할 수 있다.
df = pd.DataFrame({
    "x":[0,1,2,3],
    "p":[0.010,0.840,0.145,0.005]
})

# 기댓값 계산
df["xp"] = df["x"] * df["p"]
E = df["xp"].sum()

# x^2 계산
df["x2"] = df["x"]**2
df["x2p"] = df["x2"] * df["p"]

# E(X^2)
E2 = df["x2p"].sum()

# 분산
Var = E2 - E**2

# 표준편차
Std = Var**0.5

print(df)
print("기댓값:",E)
print("분산:",Var)
print("표준편차:",Std)



# 예제 5
# 확률변수 X의 확률밀도함수가
# f(x) = 3x^2 (0 < x < 1) 일 때
#
# 1. X의 평균 E(X)와 분산 Var(X)를 구하시오.
# 2. Y = 4X + 2 일 때 Y의 분산 Var(Y)를 구하시오.
#
# 성질: Var(aX + b) = a^2 Var(X)

x = sp.symbols('x')

# 확률밀도함수
f = 3*x**2

# E(X)
E_X = sp.integrate(x*f, (x, 0, 1))

# E(X^2)
E_X2 = sp.integrate(x**2*f, (x, 0, 1))

# X 분산
Var_X = E_X2 - E_X**2

# Y 분산
Var_Y = 16 * Var_X

# pandas로 정리
df = pd.DataFrame({
    "항목": ["E(X)", "Var(X)", "Var(Y)"],
    "값": [E_X, Var_X, Var_Y]
})

print(df)



# 예제 6
# 확률변수 X의 확률밀도함수가 f(x) = 3x^2 (0 < x < 1) 일 때
#
# 1. E(X)와 E(X^2)를 구한다.
# 2. Var(X) = E(X^2) - (E(X))^2 로 X의 분산을 구한다.
# 3. Y = 4X + 2 일 때
#    E(Y) = 4E(X) + 2
#    E(Y^2)를 계산한다.
# 4. Var(Y) = E(Y^2) - (E(Y))^2 로 Y의 분산을 구한다.

# 변수 선언
x = sp.symbols('x')

# 확률밀도함수
f = 3 * x**2

# E(X)
E_X = sp.integrate(x * f, (x, 0, 1))

# E(X^2)
E_X2 = sp.integrate(x**2 * f, (x, 0, 1))

# Var(X)
Var_X = E_X2 - E_X**2

# Y = 4X + 2
E_Y = 4 * E_X + 2

# Y^2 계산
Y = 4*x + 2
E_Y2 = sp.integrate(Y**2 * f, (x, 0, 1))

# Var(Y)
Var_Y = E_Y2 - E_Y**2

# Pandas로 정리
df = pd.DataFrame({
    "항목": ["E(X)", "E(X^2)", "Var(X)", "E(Y)", "E(Y^2)", "Var(Y)"],
    "값": [E_X, E_X2, Var_X, E_Y, E_Y2, Var_Y]
})
print(df)

#초 간단 코드
x = sp.symbols('x')
f = 3*x**2

E_X = sp.integrate(x*f, (x,0,1))
E_X2 = sp.integrate(x**2*f, (x,0,1))

Var_X = E_X2 - E_X**2
Var_Y = 16 * Var_X

df = pd.DataFrame({
    "항목": ["Var(X)", "Var(Y)"],
    "값": [Var_X, Var_Y]
})

print(df)