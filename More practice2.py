#문자를 입력 받고 철자를 하나씩 출력하시오.
a = input("please input the word: ")
for val in a:
    print(val)

#리스트를 정의하고 리스트 안의 문자를 하나씩 출력하시오.
a = ['apple','orange','cherry','watermelon']
for val in a:
    print(val)

#리스트를 정의하고 리스트 안의 문자를 철자 하나씩 출력하고 각 문자마다 글자 수를 출력하시오.
a = ['apple','orange','cherry','watermelon']
for val in a:
    print(val,len(val))

#문자'*'을 첫줄에는 1개, 두번째 줄에는 2개, 반복하여 열 번째 줄에는 열개를 출력하시오
a='*'
print(a)
for i in range(9):
    a+='*'
    print(a)

#Prime Number(소수)확인
a=int(input("please input the number: "))
b=0
for i in range(2,a): #2부터 a-1까지가 반복문의 범위이므로
    if a%i==0:
        b==1
if b==0:
    print(a,"는 소수가 아닙니다.")
else :
    print(a,"는 소수입니다.")

#1과 100사이의 5의 배수를 출력하시오.
a=1
while 1<=a<=20:
    print(a*5)
    a+=1

#사용자가 프로그램을 종료 요청할 때 "y"를 입력할 떄까지 반복해서 물으시오.
while(True):
    a = input("프로그램을 종료하시겠습니까?: ")
    if a=="y":
        break

#맞는 패스워드를 입력할 때까지 반복하기
while(True):
    a = input("pleas input your password: ")
    if a=="orange":
        break

#패스워드를 3회 이상 틀리면 반복 기회 박탈하기
a=int(input('패스워드를 입력하십시오: '))
count=1
while (a!=1234 and count<=3):
    count+=1
if count>3:
    print('패스워드를 3회 이상 틀려 처리할 수 없습니다.')
else :
    print('패스워드를 정확히 입력하셨습니다.')

