#예제1)list item 수를 입력받고 list를 생성한다. item 수만큼 반복해서 값을 입력받는다. 
# +를 활용해서 list에 추가한다. 전체 리스트를 출력한다.
item=int(input())
List=[]
while item>0:
    List_item=int(input('수를 입력하시오: '))
    List+=[List_item]
    item-=1
print(List)

#에제2)문자를 입력 받고 'b'로 시작하는 문자열을 찾아서 삭제
Str=input()
i=0
while i<len(Str):
    if Str[i]=='b':
        print(Str[0:i]+Str[i+1:])
    i+=1

#list s를 활용하여 성을 입력하면 성적이 출력되도록 하시오
s=[['kim',90],['park',89],['choi',76]]
while True:
    name=input()
    if name=='kim':
        print(s[0][1])
        break
    elif name=='park':
        print(s[1][1])
        break
    else:
        print(s[2][1])
        break
