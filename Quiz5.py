from random import randint
sum = 0 #총 탑승승객 수
for passenger in range(1,51):
    time = randint(5,50)
    if 5 <= time <= 15 :
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(passenger,time))
        sum +=1 #누락부분
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(passenger,time))
print("총 탑승 승객 : {0} 분".format(sum)) #누락부분(전체합 sum)