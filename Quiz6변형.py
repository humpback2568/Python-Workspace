def std_weight(height,gender): #1
    if gender == "여성":
        return height*height*21
    else :
        return height*height*22

height = 180
gender = "남성"
weight = round(std_weight(height/100,gender),3) #값을 넣을때 #1양식을 그대로 따름
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))