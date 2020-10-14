class SoldoutError(Exception):
    def __init__(self, msg):
         self.msg=msg
    
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1
while (True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order > chicken :
            print("재고가 부족합니다.")
        elif order <= 0 :
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting,order))
        waiting += 1
        chicken -= order
        if chicken == 0:
            raise SoldoutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    
    except SoldoutError as err:
        # init 하고 msg(메세지)넣을거면 raise에 넣고 except SoldoutError에서 "as err"를 받고 print(err)를 꼭하자
        print(err)
        break
        

    