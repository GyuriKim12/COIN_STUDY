#1번)사용자에게 이름과 나이를 입력 받아서 age에 추가. 특정한 사람의 이름을 입력 받아서 나이 출력
def add_age(n):
    age={}
    for i in range(n):
        name=input('이름을 입력하시오:')
        desc_age=input('나이를 입력하시오: ')
        age[name]=desc_age
    a=input('이름을 입력하시오: ')
    print(age[a])

n=int(input())
add_age(n)

#1번-함수 미사용
age={}
n=int(input())

for i in range(n):
    name=input('이름을 입력하시오:')
    desc_age=input('나이를 입력하시오: ')
    age[name]=desc_age

a=input('이름을 입력하시오: ')
print(age[a])
