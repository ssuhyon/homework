# 숙제 - 70
# hi 함수를 호출 시 hi 출력
def hi():
    print('hi')
hi()
# 숙제 - 71
# hi 함수 호출 사 hi "여러분들의 이름"
def hi(name):
    print(f'hi "{name}"')
hi('수현')
# 숙제 - 72
# 사용자가 입력한 두 개의 숫자를 받아 더해주는 함수 만드세요
def plus():
    a = int(input("첫번째 숫자 입력 : "))
    b = int(input("두번째 숫자 입력 : "))
    return a + b
result = plus()
print(result)

# 숙제 - 73
# 1000개 이상의 숫자를 받아 더해주는 함수 만드세요
def chungea(*args):
    return sum(args)

result = chungea(1,2,3,4,5,6,7,8,9,10,11,12)
print(result)

