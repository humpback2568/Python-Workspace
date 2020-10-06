# sales =int(input("이번 달 판매량은 어떻습니까?"))
# if 100 <= sales:
#     print("예상보다 많이 팔렸습니다.")
# elif 50<=sales<100 :
#     print("예상과 같이 팔렸습니다.")
# elif 30<=sales<50:
#     print("예상보다 적은 수치입니다. 판매마케팅 및 타겟 선정의 재검토를 바랍니다.") 
# else :
#     print("예상에 미치지 못한 수치입니다. 2차를 고려할 수 없습니다.")

# for 곱 in range(1,6):
#     print("--{}단--".format(곱))

#     for H in range(1,6):
#         print("{}*{}={}".format(곱,H,곱*H))

# #while문
# customer= "짱구"
# person="unknown"
# while person != customer :
#     print("{0}님, 김밥이 준비되었습니다.".format(customer))
#     person= input("What's your name? ") 

# sleep = [3,7]
# knockout = [5]
# for pokemon in range (1,9):
#     if pokemon in sleep:
#         continue
#     elif pokemon in knockout:
#         print("{}는 기절했다. 눈앞이 깜깜해졌다!".format(pokemon))
#         break
#     print("{0}, 너로 정했다!".format(pokemon))

# pokemon = [1,2,3,4,5,6,7,8,9]
# # print(pokemon)
# pokemon = [i+100 for i in pokemon]
# print(pokemon)

# pokemon = ["Pairi","Ggobugi","Yisanhaessie"]
# pokemon = [len(i) for i in pokemon]
# print(pokemon)

# pokemon = ["Pairi","Ggobugi","Yisanhaessie"]
# pokemon = [i.upper() for i in pokemon]
# print(pokemon)

#-------------------함수--------------- 다음에 다시 보기(함수 이해 안됨)
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance,money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else: #잔액이 출금보다 적으면
        print("출금이 완료되지않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #밤에 출금
    commission = 100 #수수료값=100
    return commission, balance - money- commission #튜플형식(튜플은 끝에 잔액과 함께 수수료추가한것(중간에수수료추가))

balance = 0 #잔액
balance = deposit(balance,1000)
# balance = withdraw(balance,300)
commission, balance = withdraw_night(balance, 700)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission,balance)) 
#윗줄에서 튜플방식으로 balance값을 withdraw한 값이며 300 출금한다고 정의했기에 여기서 balance - money- commission라고 할 필요가 없음