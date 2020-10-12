class House:
    def __init__(self,location,htype,dtype,price,completionyear):
        self.location= location
        self.htype= htype
        self.dtype= dtype
        self.price= price
        self.completionyear= completionyear

    def show_detail(self):
        print(self.location,self.htype,self.dtype,self.price,self.completionyear)

houses = []
house1 = House("마포","아파트","매매", "13억", "2003년")

houses.append(house1)

print("총 매물은 {0}대입니다.".format(len(houses)))
for house in houses:
    house.show_detail()