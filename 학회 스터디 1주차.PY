#입력 받은 숫자를 짝수와 홀수로 구분하기
a=int(input('please input the number a: '))
if a%2==1:
    print('a는 홀수입니다')
else :
    print('a는 짝수입니다')

#입력 받은 세 숫자 x,y,z중 가장 작은 수 찾기, (조건 :x,y,z는 같지 않다)
x=int(input('please input the number x: '))
y=int(input('please input the number y: '))
z=int(input('please input the number z: '))
if x>y>z:
    print('x is the least number.')
elif x>z>y:
    print('y is the least number.')
elif y>x>z:
    print('z is the least number.')
elif y>z>x:
    print('x is the least number.')
elif z>x>y:
    print('y is the least number.')
else :
    print('x is the least number.')

#입력 받은 수가 2와 3을 약수로 가지는 지 확인
A=int(input('please input the number A: '))
if (A%2==0 and A%3==0):
    print('A는 2와 3을 약수로 가집니다.')
elif (A%2!=0 or A%3!=0):
    print('A는 2와 3을 약수로 가지지 않습니다.')
else :
    print('A는 2와 3을 약수로 가지지 않습니다.')

