#1
x='z'
x*=3
print(x)

#2
print(1+1*3==6)

#3
x,y=4,2
print(not 1+1==y or x==4 and 7==8)

#4
print(5+3//4-7**2+6*8)

#5
a='abdec'
print(a[-5])
print(a[3])

#6
print(True or not True and False or False)

#7 11과 12의 배수를 출력하는 프로그램을 만드시오
x=1
while True:
    if (x%11==0 and x%12==0):
        break
    x+=1
print(x,'is divisible by 11 and 12')

x=1
while (x%11!=0 or x%12!=0):
    x+=1
print(x,'is divisible by 11 and 12')

#8
x=6
for j in range(x):
    for i in range(x):
        print(j,i)
        x=3

#8-1
x=4
for j in range(x):
    for i in range(x):
        print(j,i)
        x=2

#9
x='*'
for i in range(0,10):
    x+='*'
    print(x)
#처음에 0으로 들어왔으니까 첫번째 print(x)는 0이 나오는데 두번째일때는 x+='*'의 영향으로 
#print(x)가 **이 나오게 됨. 
# range(0,10)이면 총 10개의 문장이 나올 것 이므로 *이 2개부터 11개 까지 나옴. 
#이 것은 print(i)가 아니라 print(x)인 변수를 출력해내는 것이므로 반복문이 실행되면서 변수가 계속 변하는 것임.

x='*'
print(x)
for i in range(1,10):
    x+='*'
    print(x)
#두번째 줄에 있는 print(x)의 영향으로 *이 나옴. 
#prange(1,10)이므로 총 9문장이 나올 것이므로 *이 2부터 10까지가 출력됨.

#10
x=4
for i in range(0,x):
    i+=1
    print(i)
#위와 다르게 print(i)를 출력해 내는 것임. i+=1이 없었다면 0,1,2,3이 출력됬을 것이지만 i+=1의 영향으로 1,2,3,4가 출력됨.

#11 근사 알고리즘을 이용하여 x의 제곱근의 근사값을 구하는 알고리즘
x=25
epsilon=0.01 #오차범위는 0.01
step=epsilon**2
numGuesses=0 #count개념
ans=0.0
while (abs(ans**2-x)>=epsilon and ans<=x): #abs:절댓값
    ans+=step
    numGuesses+=1
print('numGuesses =',numGuesses)
if abs(ans**2-x)>=epsilon:
    print('Failed on square root of',x)
else:
    print(x,'is close to square root of',x)

#12 이진탐색을 이용하여 x의 제곱근의 근사값을 구하는 알고리즘
x=25
epsilon=0.01
numGuesses=0
low=0.0
high=max(1.0,x)
ans=(low+high)/2.0
while abs(ans**2-x)>=epsilon:
    print('low =',low,'high =',high,'ans =',ans)
    numGuesses+=1
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans=(low+high)/2.0
print('numGuesses =',numGuesses)
print(ans,'is close to squar root of',x)

#근사 알고리즘
x=25
epsilon=0.01
step=epsilon**2
numGuesses=0
ans=0.0
while (abs(ans**2-x)>=epsilon and ans<=x):
    ans+=step
    numGuesses+=1
print('numGuesses =',numGuesses)
if abs(ans**2-x)>=epsilon:
    print('Failed on square root of',x)
else:
    print(ans,'is close to square root',x)

#이진탐색
x=25
epsilon=0.01
low=0.0
high=max(1.0,x)
ans=(low+high)/2.0
numGuesses=0
while abs(ans**2-x)>=epsilon:
    print('low =',low,'high =',high,'ans =',ans)
    numGuesses+=1
    if ans**2<x:
        low=ans
    else:
        high=ans
        ans=(low+high)/2.0
print('numGuesses =',numGuesses)
print(ans,'is close to square root of',x)

#세제곱근 구하기 for문 사용
x=int(input('Enter an integer: '))
for ans in range(0,abs(x)+1):
    if ans**3>=abs(x):
        break
if ans**3!=abs(x):
    print(x,'is not perfect cube')
else:
    print('Cube root of',x,'is',ans)

#세제곱근 구하기 근사 알고리즘
x=64
epsilon=0.01
step=epsilon**3
numGuesses=0
ans=0.0
while (abs(ans**3-x)>=epsilon and ans<=x):
    ans+=step
    numGuesses+=1
print('numGuesses=',numGuesses)
if abs(ans**3-x)>=epsilon:
    print('Failded to square root of',x)
else:
    print(ans,'is close to square root of',x)