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
