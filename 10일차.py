#피카츄 : 전기쥐, 전기, 스타팅

# name = "피카츄"
# hp = 35
# damage = 55
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력은 {1}\n".format(hp,damage))

# #치코리타: 잎사귀, 풀, 스타팅
# chico_name = "치코리타"
# chico_hp = 45
# chico_damage = 49 
# print("{0} 유닛이 생성되었습니다.".format(chico_name))
# print("체력 {0}, 공격력은 {1}\n".format(chico_hp,chico_damage))

# def attack(name,location,damage):
#     print("{0} : {1} 체육관에 출전합니다. [공격력 {2}]".format(\
#         name,location,damage))

# attack(name, "금빛시티",damage)
# attack(chico_name,"보라시티",chico_damage)

# pokemon1= Unit("파오리",52,95)
#객체 파오리, 클래스에서 만들어 지는 애들 
#유닛 클래스의 인스턴스 = 파오리
#init함수에서 정의된 변수(name,hp,damage(self는 각 변수가 이 함수에 되기 위한 관계변수))
#멤버변수 = name,hp,damage class내에 정의된 함수 (사용,초기화 등)
#객체 외부의 변수를 할당시킬 수 있음

# pokemon1 = Unit("창파나이트",62,135)

# pokemon2 = Unit("야생의 창파나이트",62, 128)
# pokemon2.leek = True
# if pokemon2.leek == True:
#     print("{0}는 현재 '대파'를 소유하고 있지 않습니다.".format(pokemon2.name))

# mew =AttackUnit("뮤",100,100)
# mew.attack("블루")
# mew = MetamorAttackunit(mew.name,100,100,"가재장군")
# mew.transform(mew.name,"")
# mew.underattack(40)
# mew.underattack(40)
# mew.underattack(40)

class Unit: #부모 클래스 다중상속이란 부모가 여러명()
    def __init__(self,name,hp,speed): #생성자
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,enamy):
        self.enamy = enamy
        print("[선공 포켓몬]")
        print("{0} : {1} 상대로 선공을 가져갑니다. [속도 {2}]"\
            .format(self.name,enamy,self.speed))
class AttackUnit(Unit): #자식 클래스
    def __init__(self,name,hp,speed,damage): #생성자
        Unit.__init__(self,name,hp,speed)
        self.damage = damage
        
    def attack(self,locaton):
        print("{0} : {1} 체육관에 출전합니다. [공격력 {2}] [체력 {3}]".format(\
         self.name,locaton,self.damage,self.hp))
    
    def underattack(self,damage2):
        print("{0} : {1} 피해를 입었다.".format(self.name,damage2))
        self.hp -= damage2
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0}의 체력이 {1}이 되어 기절해버렸다!".format(self.name,self.hp))
#변신하는 포켓몬
class Metamor:
    def __init__(self, trans_unit):
        self.trans_unit = trans_unit
    
    def transform(self,name,trans_unit):
        print("{0} : {1}로 변신했다!".format(self.name,self.trans_unit))

#변신하면서 공격가능한 포켓몬 = 뮤
class MetamorAttackunit(AttackUnit,Metamor):
    def __init__(self, name, hp, damage,speed,trans_unit):
        AttackUnit.__init__(self,name,hp,speed,damage)
        Metamor.__init__(self,trans_unit)

electrode =AttackUnit("붐볼",60,150,50)
mew =MetamorAttackunit("뮤",100,100,100,"이브이")

electrode.move("창파나이트")
mew.transform(mew.name,"")