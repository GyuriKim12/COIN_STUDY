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

#2번
def add_age(n):
    age={}
    for i in range(n):
        name=input('이름을 입력하시오:')
        desc_age=int(input('나이를 입력하시오: '))
        age[name]=desc_age
    return age

def ages(dic):
    a=input('이름을 입력하세요: ')
    age1=dic[a]//10
    age2=dic[a]%10
    ages=''
    if 0<=age2<=2:
        ages='초반'
    elif 3<=age2<=6:
        ages='중반'
    else:
        ages='후반'
    print(a,':',str(age1)+'0대',ages)
    

n=int(input())
dic1=add_age(n)
dic2=ages(dic1)

#3번
Dic={}
for i in range(5):
    name=input('선생님 성함을 입력하시오: ')
    subjectlist=[]
    n=int(input('선생님의 과목 수를 입력하시오: '))
    if n==1:
        subjuct=input('교과목을 입력하시오: ')
        Dic[name]=subject
    else:
        for i in range(n):
            subject=input('교과목을 입력하시오: ')
            subjectlist.append(subject)
        Dic[name]=subjectlist

a=input('입력하시오: ')
if a in name:
    print(Dic[a])
else:
    namelist=[]
    for i in Dic.keys():
        if a in Dic[i]:
            namelist.append(i)
    if namelist!=[]:
        print(namelist)
    else:
        print('해당과목을 가르치는 선생님은 없습니다.')