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

# 숙제 - 74
# 리스트를 받은 뒤 그 길이를 반환하는 함수를 만드세요
def banhwan(list):
    return len(list)

# 예제 리스트
ex_list = [1, 2, 3, 4, 5]

# 함수 호출
result = banhwan(ex_list)
print(result)  # 5

# 숙제 - 75
# 세개의 숫자를 비교하여 큰 숫자를 반환하는 함수
# 예시) 
# 입력 -> func(50, 44444, 9)
# 출력 -> 44444
def jeilbig(a,b,c):
    return max(a,b,c)

# 숙제 - 76
# 20세 이상이면 True, 미만이면 False로 반환하는 함수
def doragara(age):
    if age>=20:
        return True
    return False
# def doragara(age):
#     return age >= 20

# 숙제 - 77
# 문자열의 첫 문자가 대문자인지 확인하는 함수
def hwagin(a):
    return a[0]==a[0].upper()

# 숙제 - 78
# 문자열에서 모음의 개수를 세어 반환하는 함수
def moem(mal):
    moems = "aeiouAEIOU"
    count = 0
    for i in mal:
        if i in moems:
            count += 1
    return count

# 숙제 - 79
# 숫자 리스트에서 짝수만 합을 계산하는 함수 
def zzagsu(numlist):
    hab = 0
    for num in numlist:
        if num % 2 == 0:
            hab += num
    return hab
    
# 숙제 - 80
# 리스트와 특정 값을 받아 그 리스트에 그 값이 포함되어 있는지 확인하는 함수
def itzi(list,a):
    return a in list

# 숙제 - 81
# 두 개의 문자열을 받아 공통으로 포함된 문자를 반환하는 함수를 만드세요
def gongtong(a, b):
    result = ''
    for x in a:
        if x in b and x not in result:
            result += x
    return result

# 숙제 - 82
# 문자열을 받아 문자를 반대로 반환하는 함수를 만드세요
def bandea(a):
    return a[::-1]

# 숙제 - 83
# 삼각형의 밑변과 높이를 입력 받아 삼감형의 넓이를 계산하는 함수 만드세요
def nerby(x,y):
    return x * y * 0.5

# 숙제 - 84
# 리스트를 받아 중복된 요소가 있는지 확인하는 함수
def jungbok(list):
    return len(list) != len(set(list))

# 숙제 - 85
# 두개의 리스트를 받아 공통 요소만 반환하는 함수
def gt_yoso(list1, list2):
    gtys = []
    for x in list1:
        if x in list2 and x not in gtys:
            gtys.append(x)
    return gtys
    
# 숙제 - 86
# 문자열에서 숫자만 추출하는 함수
def chuchul(munjayul):
    result = ''
    for i in munjayul:
        if i.isdigit():
            result += i
    return result
def chuchul1(munjayul):
    return ''.join([i for i in munjayul if i.isdigit()])


# 숙제 - 87
# 리스트(숫자)에서 최대값과 최솟값의 차이를 계산하는 함수
def gyesan(list):
    return max(list)-min(list)