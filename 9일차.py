# import sys
# print("지영","영희","지현", sep=",", end="?")
# print("누가 이길까요?")

# individual_values ={"피카츄":25, "거북왕":325,"펜드라":429}
# for pokemon, value in individual_values.items():
#     print(pokemon.ljust(6),str(value).rjust(5),sep=":")

#솜사탕 대기순번표
# for num in range(1,35):
#     print("대기번호 : "+str(num).zfill(4))

# answer = input("검색하고 싶은 포켓몬을 입력하십시오 :")
# print("입력하신 포켓몬은 " + answer + " 입니다.")

# print("{0:1>7}".format(325))
# print("{0: >+7}".format(-325))
# print("{0:_<+10}".format(-2568))
# print("{0:+,}".format(-25685682568314))
# print("{0:^<+30,}".format(3141592653589793))
# print("{0:f}".format(22/7))
# print("{0:.3f}".format(22/7))

# base_stats = open("stat.txt","w",encoding="utf8") 
# #기록되는방식=.txt, 쓰기(덮어쓰기)방식, 한글인코딩
# print("피카츄 : 320", file=base_stats)
# print("라이츄 : 485", file=base_stats)
# base_stats.close()

# base_stats = open("stat.txt","a",encoding="utf8")
# #이어쓰기 up and ="a"
# base_stats.write("망냐뇽 : 600")
# base_stats.write("\n성원숭 : 455")
# base_stats.close()

# base_stats = open("stat.txt","r",encoding="utf8")
# print(base_stats.read())
# base_stats.close()

# base_stats = open("stat.txt","r",encoding="utf8")
# print(base_stats.readline(),end="")
# print(base_stats.readline())
# print(base_stats.readline())
# print(base_stats.readline())
# base_stats.close()

# base_stats = open("stat.txt","r",encoding="utf8")
# while  True:
#     line = base_stats.readline()
#     if not line :
#         break
#     print(line,end="")
# base_stats.close()

# base_stats = open("stat.txt","r",encoding="utf8")
# lines =base_stats.readlines()
# for x in lines :
#     print(x, end="")
# base_stats.close() #open만 해두면 다른user가 사용불가할수도 있으니 base_stats.close() 꼭하자

# import pickle
# base_stats = open("base.pickle","wb")
# base = {"이름":"홍수몬","HP":50,"기술":["메가톤펀치","인파이트","카운터","퍼스트가드"]}
# print(base)
# pickle.dump(base,base_stats) #base 정보를 base stats.file에 저장
# base_stats.close()

# base_stats = open("base.pickle","rb") #wb가 아닌 rb 쓰기바이너리가 아닌 읽기 바이너리 바이너리는 이진코드로 저장되는형식
# base = pickle.load(base_stats)
# print(base)
# base_stats.close()

# import pickle

# with open("stats.pickle", "rb") as base_stats:
#     print(pickle.load(base_stats))

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬 공부중!!!")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())