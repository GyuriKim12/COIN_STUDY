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