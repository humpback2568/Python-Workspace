# import pickle
# num = 0
# while True:
#     num +=1
#     with open(str({num})+"주차.txt".format(num),"w", encoding="utf8") as number_file:
#         number_file.write("- "+ str({num})+"주차 주간보고 - \n부서 :\n이름 :\n업무 요약 : ")
#         if num == 50:
#             break

import pickle
num = 0
while True:
    num += 1
    with open(str({num})+"보고서.txt".format(num),"w", encoding="utf8")as report_file:
        report_file.write("- "+str({num})+"주차 주간보고 - \n부서 :\n이름 :\n업무 요약 : ")
        if num == 10:
            break