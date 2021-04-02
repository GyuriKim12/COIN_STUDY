# 실습1) 두 개의 숫자를 입력 받으면 두 수를 더하여 반환하는 함수 my_plus 함수를 정의하시오
def print_numbers():
    result=a+b
    print('Result is',a+b)
a,b=map(int,input('Input two numbers: ').split())
print_numbers()

# 실습 2) 두 개의 숫자를 입력 받으면 두 수를 빼고, 곱하고, 나누는 
# 함수 my_minus, my_multiply, my_division 함수를 정의하시오
def print_numbers():
    my_minus=a-b
    my_multiply=a*b
    my_division=a/b
    print('Minus result is',a-b)
    print('Multiply result is',a*b)
    print('Division result is',a/b)
a,b=map(int,input('Input two numbers: ').split())
print_numbers()

# 실습 3) 두 개의 숫자와 +,-,*,/기호 중 하나를 입력 받으면 입력 받은 기호에 따라 앞에서 선언한 
#my_plus, my_minus등의 함수를 적절히 사용하여 연산을 수행할 수 있도록 돕는 my_calculate함수를 선언하시오.
def my_calculate():
    my_plus=a+b
    my_minus=a-b
    my_multiply=a*b
    my_division=a/b
    if val=='+':
        print('Result is',my_plus)
    elif val=='-':
        print('Result is',my_minus)
    elif val=='*':
        print('Result is',my_multiply)
    else:
        print('Result is',my_division)

a,b=map(int,input('Input two numbers: ').split())
val=input('Input operation: ')
my_calculate()