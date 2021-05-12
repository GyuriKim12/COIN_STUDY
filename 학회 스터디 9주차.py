#1번
def generateDictionary(n):
    Dic={}
    for i in range(n):
        word=input('프로그래밍 언어 이름: ')
        desc=input('프로그래밍 언어 설명: ')
        Dic[word]=desc
    return Dic

n=input('Input number of programming languages: ')
print(generateDictionary(n))

#1번 확장
def generateDictionary(n):
    Dic={}
    for i in range(n):
        word=input('프로그래밍 언어 이름: ')
        desc=input('프로그래밍 언어 설명: ')
        Dic[word]=desc
    return Dic

def printDictionary(*dics):
    for dic in dics:
        for word in dic:
            print(word,':',Dic[word])

n=input('Input number of programming languages: ')
dic1=generateDictionary(n)
dic2=generateDictionary(n)
print(printDictionary(dic1,dic2))

#2번
def generateDictionary(n):
    Dic={}
    for i in range(n):
        word=input('프로그래밍 언어 이름: ')
        desc=input('프로그래밍 언어 설명: ')
        Dic[word]=desc
    return Dic

def translateDictionary(dic):
    new_dic={}
    for i in range dic:
        print('======================')
        print('description: ',dic[word])
        new_word=input('Input the name of the languagein English: ')
        new_dic[new_word]=desc
    return new_dic

n=input('Input number of programming languages: ')
dic1=generateDictionary(n)
dic2=translateDictionary(dic1)
print(dic1)
print(dic2)

#2번 확장
def generateDictionary(n):
    Dic={}
    for i in range(n):
        word=input('프로그래밍 언어 이름: ')
        desc=input('프로그래밍 언어 설명: ')
        Dic[word]=desc
    return Dic

def translateDictionary(dic):
    new_dic={}
    for i in range dic:
        print('======================')
        print('description: ',dic[word])
        new_word=input('Input the name of the languagein English: ')
        new_desc=input('Input the description if the language in English: ')
        new_dic[new_word]=new_desc
    return new_dic

n=input('Input number of programming languages: ')
dic1=generateDictionary(n)
dic2=translateDictionary(dic1)
print(dic1)
print(dic2)

#3번
def generateDictionary(n):
    Dic={}
    for i in range(n):
        word=input('프로그래밍 언어 이름: ')
        desc=input('프로그래밍 언어 설명: ')
        Dic[word]=desc
    return Dic

def translateDictionary(dic):
    new_dic={}
    for word in dic:
        print('======================')
        print('description: ',dic[word])
        new_word=input('Input the name of the languagein English: ')
        new_desc=input('Input the description if the language in English: ')
        new_dic[new_word]=new_desc
    return new_dic

def searchDictionary(*dics):
    while True:
        searchDic=[]
        a=input('Enter a word for search: ')
        for dic in dics:
            for word in dic:
                if a in dic[word]:
                    searchDic.append(word)
        if searchDic!=[]:
            print('Search result: ',searchDic)
        else:
            print('No match!! Break!')
            break
        
n=int(input('Input number of programming languages: '))            
dic1=generateDictionary(n)
dic2=translateDictionary(dic1)
searchDictionary(dic1,dic2)