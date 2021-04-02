def funcName(a,b):
    result=a+b
    return result
print(funcName(10,20))

def print_full_name(last_name,first_name):
    print(last_name,',',first_name)
print_full_name(last_name='김',first_name='규리')

def print_full_name(last_name,first_name):
    print(last_name,',',first_name)
print_full_name('김','규리')

def print_full_name(first_name,last_name):
    print(last_name+',',first_name)
print_full_name('윤수','이')

def print_full_name(first_name,last_name):
    print(last_name+',',first_name)
print_full_name('수민','이')

def fun(count):
    a=5
    count=count+a
    return count
count=0
print('result=',fun(count))
print(count)

def fun(count):
    a=5
    count=count+a
    return count
fun(0)

def fun(count):
    global a
    a=5
    count=count+a
    return count

a=0
print('result=',fun(count))
print(a)

#2개의 파라미터를 지정하여 지정한 파라미터 두개의 곱을 리턴하는 함수를 작성해라
def print_numbers(a,b):
    result=a*b
    return result

print_numbers(10, 5)

#월급 계산 프로그램 만들기
#근무 시간이 40시간을 초과하면 초과 근무 시간에는 시급의 1.5배를 지급한다
def computepay(hour,rate):
    if hour>40:
        print('pay :',40*int(rate)+(int(hour)-40)*1.5*int(rate))
    else:
        print('pay =',int(hour)*int(rate))
coumptupay(45,10)