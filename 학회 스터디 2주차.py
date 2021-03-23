#프로그램 사용자로부터 임의의 문자열을 입력 받고, 입력 받은 문자열의 길이를 출력하시오. 또한, 입력 받은 문자열 중 영문 소문자의 개수를 세어 출력하시오.
#1
str1=input("문자열을 입력해 주세요: ")
length=len(str1)
print(length)
i=0
count=0
while i<length:
    if str1[i].islower()==True:
        count+=1
    i+=1
print(count)

str1=input("문자열을 입력해 주세요: ")
length=len(str1)
print(length)
i=0
coun=0
for i in range(len(str1)):
    if str[i].islower()==True:
        count+=1
print(count)


#프로그램 사용자로부터 3개의 문자열을 입력 받고, 이를 모두 합쳐 하나의 문자열로 출력하는 프로그램을 작성하시오.
str1, str2, str3 = input("3개의 문자열을 공백을 기준으로 입력하세요: ").split()
print(str1+str2+str3)

#프로그램 사용자로부터 문자열을 입력 받고, 영문 소문자'a'가 처음 등장하는 곳 다음부터 'z'가 등장하기 전까지의 문자열만 필터링하여 출력하시오.
#단,'a'는 반드시 'z'전에 입력되어야 하며, 'a'와 'z'는 문자열 중에 반드시 포함되어야 한다.
A = input('문자열을 입력하시오(a와 z포함,a가 z보다 먼저 나와야함): ')
a = A.find("a")
z = A.find("z")
print(A[a:z])