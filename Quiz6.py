def std_weight(height, gender):
    if gender =="남자":  #우선 남자 여자를 가리기 위해서 if로 나눔
        return  height*height*22
    else :
        return  height*height*21

height= 175
gender ="남자"
weight = round(std_weight(height/100, gender),2)     #들어가는 값은 위의 지역변수 std가 아닌 아래서정의한 그냥 weight변수 반올림은 round(값,2) 
print("키 {0}cm {1}의 표준 체중은 {2} kg 입니다.".format(height,gender,weight))