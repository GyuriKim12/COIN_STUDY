#임의의 정수 10개를 가진 리스트 변수를 선언하고 순회 하면서, 70점 이상의 점수에는 점수와 함께
#면허증 발급 결정을 출력하고 
# 그 외에는 점수와 함께 면허증 발급 취소를 출력하는 프로그램을 작성하시오
a=[10,66,82,79,68,25,98,85,50,41]
for i in range(len(a)):
    if a[i]>=70:
        print(a[i],'면허증 발급이 결정되었습니다.')
    else:
        print(a[i],'면허증 발급이 취소되었습니다.')

#1번과 다르게 사용자로부터 정수를 입력 받아 리스트에 담을 수 있도록 프로그램을 리팩토링하시오.
#단, 사용자로부터 입력받는 정수는 EOF라는 문자열을 입력 받기 전까지만 입력 받으시오.
#(hint: 리스트 객체 numbers.append()활용. while(1)문에서 빠져나가는 방법은 break)
numbers=list() 
s=int(input('정수를 입력하시오: '))
count=0
while count<=9:
    s=int(input('정수를 입력하시오: '))
    numbers.append(s)
    if s=='EOF':
        break
    count+=1
print(numbers)
for i in range(len(numbers)):
    if numbers[i]>=70:
        print(numbers[i],'면허증 발급이 결정되었습니다.')
    else:
        print(numbers[i],',면허증 발급이 취소되었습니다.')

#for반복문을 이용하여 1단부터 9단까지의 구구단을 출력하시오
for j in range(1,10):
    for i in range(1,10):
        print(j*i)