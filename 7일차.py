#함수
# def profile(name, type,move1,move2,move3,move4):
#     print("이름 : {0}\t타입 : {1}\t"\
#         .format(name, type),end=" ")
#     print(move1,move2,move3,move4)

# profile("라프라스","물,얼음","멸망의노래","파도타기","잠자기","눈싸라기")

# def profile(name, type,*moves):
#     print("이름 : {0}\t타입 : {1}\t"\
#         .format(name, type),end=" ")
#     for move in moves:
#         print(move, end=" ")

# profile("라프라스","물,얼음","멸망의노래","파도타기","잠자기","눈싸라기")
# profile("탕구리","땅","뼈다귀던지기","날뛰기")

# def profile(name, type="노말",main_move="파괴광선"):
#     print("이름 : {0}\t타입 : {1}\t주 기술 : {2}"\
#         .format(name, type,main_move))

# profile("피카츄")
# profile("펜드라")
# profile("라프라스")

# def profile(name, type,main_move):
#     print(name, type,main_move)

# profile(main_move="메가폰",type="독,벌레",name="펜드라")

lab = 150 #1

# def league(pokemons):
#     global lab # lab = 150 #2
#     lab = lab - pokemons
#     print("[함수 내] 남은 포켓몬 : {0}".format(lab)) #2

def league_return(lab,pokemons): 
    lab = lab - pokemons
    print("[함수 내] 남은 포켓몬 : {0}".format(lab))
    return lab

print("전체 포켓몬 : {0}".format(lab)) #1
lab=league_return(lab,3)
# league(5)
print("전체 포켓몬 : {0}".format(lab)) #1