def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance+money

def withdraw_night(balance, money):
    commission=100
    if balance>=money+commission: # ":" 생략됐습니다
        print("출금이 완료되었습니다. 수수료 {0}원이고, 잔액은 {1}원 입니다.".format(commission, balance-money-commission))
        return commission, balance-money-commission #blance 오타났습니다
    
    else:
        print("출금불가합니다. 잔액은 {0}원 입니다.".format(balance))
        return commission, balance

balance=0
balance=deposit(balance, 1000) #일부러그러신건지 모르겠지만 잔고에 500(기준에 되는 잔고)만 부여하셔서 아래 잔액이 잘 안나옵니다
commission, balance=withdraw_night(balance, 300) #withdraw_night 함수에 commission변수도 있어서 commission도 튜플형식(?)으로 부여해야 합니다