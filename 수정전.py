def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
return balance+money

def withdraw_night(balance, money):
commission=100
if balance>=money+commission #여기서 syntax 에러 납니다 제가 봤을 때는 문제 없는 것 같습니다...
print("출금이 완료되었습니다. 수수료 {0}원이고, 잔액은 {1}원 입니다.".format(commission, balance-money-commission))
return commission, blance-money-commission
else:
print("출금불가합니다. 잔액은 {0}원 입니다.".format(balance))
return commission, balance

balance=0
balance=deposit(balance, 500)
withdraw_night(balance, 500)