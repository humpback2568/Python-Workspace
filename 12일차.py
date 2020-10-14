# import theater_module
# theater_module.price(3) #3명이서 영화보러 가는 가격
# theater_module.price_army(5)

# import theater_module as mv
# mv.price_army(8) #모듈명이 길면 as를 사용 줄이는 것 가능

# from theater_module import *
# price_morning(4)

# from theater_module import price, price_morning
# price(4)

# from theater_module import price_army as am
# am(3)

# import travel.thailand #모듈이나 패키지만 가능
# #클래스나 함수 import 불가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage #폴더명 적고 내부문서명 #1
# trip_to = ThailandPackage()
#  #trip은 내가 여기서 정의한 변수 문서명적고. 클래스
# trip_to.detail()

# from travel import vietnam #2
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# 위 아래 방식 다 가능하지만 난 아래

# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(thailand))
# print(inspect.getfile(random))

#input 사용자의 입력을 받는 함수
# language = input("What is your mother_tongue?")
# print("{0}은 아주 좋은 언어입니다.".format(language))

#dir 어떤 객체를 넘겨줬을 때 객체가 갖고 있는 함수와 변수 표시
# print(dir())
# import random
# print(dir())

# print(dir(random)) #"random" 함수 내에 있는 함수와 변수를 표시

# name = "Mike"
# print(dir(name))

#내장함수 "list of python builtins" 라고 구글에 검색하면 파이썬 내 어떤 함수가 있는지 검색 가능
#외장함수 "list of python modules"

#예제들
#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제 제공 기본기능(폴더 생성&삭제 등)
# import os
# print(os.getcwd()) #현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%H:%M:%S"))

import datetime
# print("오늘 날짜는 ",datetime.date.today())

#timedelta : 두 날짜 사이 간격
today = datetime.date.today() #오늘 날짜값을 저장
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은 ", today +td)
