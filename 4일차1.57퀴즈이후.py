# #분기 IF
# weather = input("오늘 날씨? ")
# if weather == "비"or weather =="눈":
#     print("우산을 챙기세요")
# else:
#     print("준비물 필요 없습니다")

temp= int(input("기온은 어때여? "))
if 30 <= temp:
    print("매우 더워요. 열사병에 주의하세요.")
elif 10 <= temp  < 30:
    print("좋은 날씨입니다.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else :
    print("너무 춥습니다. 빙판길에 주의하세요.")
