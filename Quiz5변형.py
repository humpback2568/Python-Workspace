from random import randint
sum = 0
for pokemon in range (50,151): #for는 for기준이 이뤄지는것을 반복 for또한 if와 같이
    speed=randint(50,150)
    if 110 <= speed <= 150 :
        print("[O] {0}번째 포켓몬 (스피드 : {1})".format(pokemon,speed))
        sum +=1 #IF에 종속되어야 한다 앞으로 밀지마
    else :
        print("[ ] {0}번째 포켓몬 (스피드 : {1})".format(pokemon,speed))
print("총 선발 포켓몬 : {0}마리".format(sum))
