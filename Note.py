#!/usr/bin/env python
# coding: utf-8

# <br>
# 
# #### 0. 특정 함수에 대해 궁금할 때

# In[2]:


# Shift + Enter : 셀의 실행
# Shift + Tap : 함수 & 변수의 Docstring 확인

print() 


# In[1]:


help(print)


# In[3]:


# 이것은 주석입니다.


# <br>
# 
# #### 1. 기초 데이터 타입

# #### 정수형(int)과 실수형(float)

# In[1]:


x = 9


# In[2]:


print(x)


# In[5]:


type(x)


# In[4]:


x + 1


# In[5]:


x * 2


# In[6]:


x ** 2 # 제곱 연산


# In[15]:


x / 2 # 나누기 & 몫


# In[17]:


x % 2 # 나머지


# In[6]:


x += 1
x


# In[7]:


x *= 2 # 곱하여 변수에 그대로 담기
x


# In[7]:


y = 2.5


# In[ ]:


y. #tab 눌러보기


# In[8]:


type(y) # 어떤 타입일까요?


# In[ ]:


#점 자체가 둥둥 떠 있다 floating-point number 부동소수점


# In[9]:


# y를 정수 자료형으로 바꾸려면? 형변환 (type casting) 자료형이름을 된 함수가 거의 다 있음
int(y) # from float to integer


# In[18]:


x = 9 
float(x) 


# In[13]:


print(y, y+1, y*2, y**2)


# #### 문자열 (string)

# In[11]:


#글자들이 모여있는 줄. 글자 5개의 그룹

s = "Hello"
s


# In[10]:


type(s)


# In[12]:


len(s) # 길이를 영어로 하면? (앞 3글자)


# In[ ]:


s.


# In[23]:


s.upper()


# In[13]:


s.lower() # 모두 소문자로


# In[14]:


#문자열 포매팅
print("My name is {}".format("Groot"))


# In[ ]:


print("my name is %d" %323.435)


# In[27]:


print("Hello" + " " + "world") # 문자열 합치기


# In[11]:


temp = "Python"


# In[ ]:


temp() #함수
temp[?] #temp 변수 안에 들어가서 내용을 꺼내겠다

get_ipython().run_line_magic('pinfo', '')
get_ipython().run_line_magic('pinfo', '')


# In[12]:


temp[0]


# In[13]:


-이상 & -미만 --> 몇조각으로 나눌 때 경계값 겹치지 않도록
temp[0:4]


# In[14]:


temp[:4]


# In[5]:


temp[4:]


# In[6]:


temp[-1]


# In[31]:


temp = "Python is easy"
temp.split() # str을 특정한 문자(기본값:여백)를 기준으로 잘라내어 list로 만들어줍니다. (이 때 기준이 되는 해당 문자는 삭제됩니다.)


# In[1]:


temp = "Python is easy"
temp.split('s') # 's'를 기준으로 자르려면?


# In[15]:


temp = ['Python', 'is', 'easy']
'___'.join(temp)


# In[34]:


''.join(temp) # "Python is easy" 와 같이 합치려면?


# In[15]:


x = 214
str(x) # Integer to string


# #### 참/거짓 (bool)

# In[17]:


t = True
f = False


# In[18]:


type(t) #boolean


# In[38]:


print(t and f)


# In[39]:


print(t or f)


# In[40]:


print(not t)


# <br>
# 
# #### 2. 함수 (function, method)

# In[22]:


# 두 변수(파라미터)를 받아 합을 돌려주는 함수 add_nums 만들기

#Python에서는 한 덩어리라는 것을 알려주기 위해 '콜론과 들여쓰기'를 쓴다. 다른 언어는 {}
#들여쓰기 안 해보고 오류메시지 읽어보기

def add_nums(num1, num2):  #parameter, 매개변수
    return num1+num2

def add_nums2(num1, num2=10):
    return num1+num2


# In[26]:


print(add_nums(2, 3)) #argument, 인자 (밖에서 던져주는 값)
print(add_nums2(2))


# In[25]:


print(1, end='__') #shift+tab으로 함수기능 체크하고 default값 수정해보기
print(2, end='__')
print(3, end='__')


# In[27]:


# Quiz 1. 성과 이름을 받아 이름을 돌려주는 함수 name_creator 만들기

def name_creator(str1, str2):
    return str1 + str2


# In[28]:


name_creator("그", "루트")


# In[53]:


# Quiz 2. 다음 함수는 에러를 출력합니다. 어디를 고쳐야할까요?
def drink():
beverage = "Coke"
print(beverage)


# In[ ]:


# Quiz 3. 원의 반지름을 받아 원의 넓이를 Return 해주는 함수 circle_area 만들기 (ㅠ = 3.14)


# In[ ]:


circle_area(10)


# #### Lambda Functions

# In[144]:


def func(x):
    return x**2


# In[145]:


func(5)


# In[323]:


# x(input) 를 받아 x**2(output) 를 return 해주는 람다 함수


# In[324]:


func(5)


# <br>
# 
# #### 3. 컨테이너 (다른 변수들을 담을 수 있는 자료형)
# list, dict, tuple, set
# iterable 속성 가짐

# In[30]:


CRUD
Create
Read
Update
Delete


# In[ ]:


list
x = []

dict #중괄호는 거의 다 dict임
x = {key:value, , , }

tuple #손으로 만들 일 없음
x = ()

set
x= { , , , } || x = set(~~~)


# #### 리스트 (list)

# In[31]:


x = [3, 1, 2, 4, 6] # 리스트의 생성
type(x)


# In[20]:


x[0]


# In[33]:


x[:3] # [3, 1, 2] 를 출력하려면?


# In[34]:


x[1:] # 1부터 끝까지?


# In[60]:


x[-1] 


# In[36]:


x.append("어머나") # 리스트 item 추가하기
x


# In[147]:


# 리스트 아이템의 삭제 
# 1) 데이터의 순서/자리를 활용하여 삭제할 때 : del == index를 활용 (추천)
# 2) 데이터 값 자체를 활용하여 삭제할 때 : remove() == value를 활용


# In[37]:


del x[5] # 삭제의 영어 단어 앞 3글자? 
x


# In[39]:


x.remove(4) #4가 여러개 있다면 맨 앞에 있는 4가 없어짐
x


# In[40]:


# 리스트 합치기
y = [3, 4, 5]
z = x + y # 쉽게 생각해보세요 :)
z


# In[41]:


# 리스트 정렬하기
z.sort()
z


# In[42]:


# 리스트 역으로 정렬하기
z.sort(reverse=True) # '거꾸로' 를 영어로 하면? Shift + Tab으로 옵션 확인
z


# #### 딕셔너리 (dict)

# In[43]:


cage = {'Cat' : '야옹', 'Dog' : '멍멍'} # {key:value, key:value, ...}
cage


# In[44]:


cage['Cat'] # key 기반 호출


# In[45]:


print('Cat' in cage) # key 유무 체크 in : 멤버십 체크 연산자


# In[47]:


cage['Pig'] = '꿀꿀2' # dict에 새로운 item 추가하기, key값 중복 불가능
cage


# In[60]:


#텍스트 데이터 분석 시
word_bag = {'Cat' : 4, 'Dog' : 3}
word_bag['Tiger'] = 1
word_bag


# In[61]:


word_bag['Tiger'] += 1
word_bag


# In[48]:


del cage['Pig'] # 삭제의 영어 단어 앞 3글자? 리스트랑 같음.
cage


# #### 튜플(tuple) 
# 값과 크기가 변하지 않음

# In[49]:


t = (5, 6)
type(t)


# In[50]:


t[0]


# In[51]:


# 튜플이 사용되는 예시

def return_tuple(x, y):
    return x, y


# In[52]:


what = return_tuple(3, 4)
what


# #### 집합(set)
# 중복을 허용하지 않음

# In[ ]:


직접 만들 일은 없음, 중복 날리기용, 집합연산할 때


# In[53]:


s = {1, 2, 3, 3, 4, 4, 5} #중복 없음
s


# In[54]:


temp = [1, 2, 3, 3, 4, 4, 5]
temp


# In[55]:


# 리스트 temp 에서 중복을 제거하고, 다시 리스트로 만드려면?

what = list(set(temp))
what


# <br>
# 
# #### 4. 조건문과 반복문
# if, for, while

# #### if

# In[33]:


def check_price(lunch_price):
    
    if lunch_price > 10000:
        lunch_type = "프리미엄 도시락"
    elif lunch_price < 3000: 
        lunch_type = "저렴이 도시락"
    else: # 나머지 조건 모두 받기, else 뒤에는 조건식이 없음
        lunch_type = "무난무난 도시락" 
        
    return lunch_type


# In[35]:


check_price(7000)


# In[62]:


cage = ['Cat', 'Dog', 'Tiger']


# In[63]:


if 'Cat' in cage:  # Key 유무 체크
    print('야옹아 이리온')


# #### for

# In[64]:


nums = [1, 2, 3, 4, 5]


# In[65]:


for number in nums:  #돌릴 수 있는 nums
    print(number)


# In[67]:


# 숫자들의 리스트에서 1과 4가 연속으로 나오는 숫자 찾기

list_of_nums = [121142131512315, 1241561717265467, 153462615114151231, 1634263414616123, 15236172821568]
for num in list_of_nums:
    if '14' in str(num):
        print(num)


# In[68]:


range(5) # '범위'를 영어로? #iterable 속성을 가짐. 뺑뺑 돌아갈 준비가 되어있다.


# In[98]:


for index in range(5):
    print(index)


# In[3]:


class_1 = ['철수', '영희', '동수'] # 왜 에러가 발생할까요? --> 변수이름으로 예약어


# In[4]:


# enumerate 배우기 (데이터분석 때 많이 씀. '누적하다' index번호를 누적하다)

for student in class_1:
    print(student)

for student in enumerate(class_1):
    print(student)

for index, student in enumerate(class_1):
    print("얘 번호는 {}번이구요. 이름은 {}래요".format(index, student))


# In[73]:


# for 문의 주된 활용 방식

students = ['철수', '영희', '동수']

empty_list = []
for student in students:
    empty_list.append('김' + student) # 리스트에 item 추가하기


# In[74]:


empty_list


# #### while

# In[75]:


temp = 1
while temp <= 5:
    print(temp)
    temp = temp + 1 # temp 를 1 증가시켜주려면?


# In[76]:


# 무한 루프, Pass, Interrupting kernel
# 가끔 kernel restart 활용하기

while True:
    pass


# In[ ]:


# Quiz 4. 점수(0~100)를 입력으로 받아 학점을 출력해주는 함수 grade를 만드세요.


# In[ ]:





# In[ ]:


grade(87)


# In[216]:


# Quiz 5. 3개의 숫자를 입력으로 받아, 가장 큰 수를 출력하는 함수 best 를 만드세요. (Hint. 리스트와 sort()를 활용해보세요.)


# In[241]:





# In[242]:


best(20, 100, 60)


# In[251]:


# Quiz 6. 숫자 하나를 입력받아, 홀수면 "odd", 짝수면 "even"을 출력하는 함수 odd_or_even을 만드세요. (나머지 연산 명령어는?)


# In[252]:





# In[253]:


odd_or_even(9)


# In[ ]:


# Quiz 7. "20180323sunny" 와 같은 문자열을 입력받아, "Year is 2018, Day is 0323, Weather is sunny" 를 출력하는 함수 weather를 만드세요.


# In[ ]:





# In[ ]:


weather('20180323still cold')


# <br>
# 
# #### 5. 파일 읽고 쓰기

# #### 파일 쓰기

# In[78]:


file = open('cage.txt', 'w', encoding='utf-8') # '열다'를 영어로? & w/r/a
#경로명, 모드, 습관적으로 적는 인코딩 옵션
#주피터노트북 옆에 있는 cage.txt
#상위 폴더는 ../cage.txt 옆에 있는 data폴더는 data/cage.txt


# In[5]:


cage = ['Cat', 'Dog', 'Tiger']


# In[80]:


file.write(cage) # 에러가 발생했어요. 어떻게 해야할까요?


# In[81]:


for animal in cage:
    file.write(animal)


# In[82]:


file.close() # close 안 쓰면 애가 심부름 리스트 쓰고있는중.


# In[ ]:


# close를 안쓰려면?


# In[7]:


with open('cage_3.txt', 'w', encoding='utf-8') as file: #결과를 잠깐 file로 하고. with문 끝나면 file 자동으로 날림.
    for animal in cage:
        file.write(animal + '\n')


# In[ ]:





# In[114]:


# file.write(cage) 대신,
file = ?('cage.txt', 'w', encoding='utf-8') # '열다'를 영어로? & w/r/a

for animal in cage:
    file.write(animal + '\n') # \t 로 바꿔서도 실행해보세요
    
file.close()


# In[ ]:


# file = open('cage.txt', 'w', encoding='utf-8')
# file.writelines(cage)
# file.close()


# In[116]:


# 자동으로 파일 닫기 (convention)

get_ipython().run_line_magic('pinfo', 'open')
    for animal in cage:
        file.write(animal + '\n')


# #### 파일 읽기

# In[84]:


file = open('cage.txt', 'r', encoding='utf-8') # 읽기 모드 default값이 'r'이라서 따로 안 써도 되긴 함. 순서맞추면 mode 안 써도 됨


# In[85]:


cage = file.readlines() # 여러줄 한번에 읽어서 리스트에 담기 (Shift+Tap 을 사용해보세요!)
cage


# In[ ]:


print(cage[0])


# <br>
# 
# #### 6. Python 기본 내장함수와 외장함수

# In[93]:


len('Python') # 길이?


# In[94]:


list('Python')


# In[95]:


dir('Python') # (여기서는 string) 객체가 자체적으로 가지고 있는 변수나 함수
# "Python"은 'str'이라는 데이터타입(클래스)이 만들어낸 객체이며 'str' 데이터타입(클래스)에 정의된 모든 속성(객체변수)과 메소드를 상속 받음


# In[96]:


abs(-1.2) # '절대값'의 앞 3글자


# In[97]:


round(1.7) # 반올림


# In[98]:


bool(1) # 참/거짓 판별 뭐라도 들어있으면 true


# In[99]:


sum([1, 2, 3]) # 합


# In[100]:


max([1, 2, 3]) # 최대값


# In[101]:


min([1, 2, 3]) # 최소값


# <br>
# 
# #### 7. 라이브러리 활용하기 (Library == Package, Module(단일 .py)의 상위 개념 )

# In[10]:


import facebook


# In[12]:


facebook.print_something()


# In[ ]:


pip install fbml==1.2.1 #버전 설정
conda install fbml
#pip 또는 conda 이름의 저장소
#conda가 안정적. 단점은 conda재단이기에 새로 나온 라이브러리 없을 수도.
#pip는 파이썬이 관리함.


# In[107]:


get_ipython().system('pip install numpy #바로 설치')


# In[ ]:


pip freeze #라이브러리 리스트 쭉 받아보기
pip freeze > lib_list.txt #라이브러리 리스트 텍스트파일로 저장
#컴퓨터 이사할 때 참고하기 좋음


# In[106]:


import fbml


# In[108]:


import numpy # import 라이브러리이름


# In[338]:


a = numpy.array([1, 2, 3])
a


# In[339]:


import numpy as np # import 라이브러리이름 as 별명 (as:앨리어스) #가장많이씀


# In[340]:


a = np.array([1, 2, 3])
a


# In[343]:


from numpy import array, ndarray # from 라이브러리이름 import 함수이름


# In[342]:


a = array([1, 2, 3])
a


# In[ ]:


from numpy import * #다 땡겨오는 거라서 위험.


# In[ ]:





# In[109]:


import random # 외장함수

x = random.random()
x


# In[110]:


x = random.randint(1,100) # 1과 100 사이의 '정수' 를 랜덤하게 뽑으려면? Shift + Tab 을 활용해보세요!
x


# In[13]:


import os # 외장함수

os.getcwd() # get current working directory


# In[ ]:




