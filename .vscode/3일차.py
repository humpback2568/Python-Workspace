'''n = "Empire State Building"
print(n.lower())
print(n.upper())
print(n[0].isupper())
print(len(n))
print(n.replace("Empire", "Emperor"))

x= n.index("i")
print(x)
x=n. index("i", x+1)
print(x)
print(n.find("Emperor"))
#print(n.index("Emperor"))

print(n.count("i"))'''
#문자열 포맷 1시간 00
'''print("나는 %dcm 입니다." %177)
print("나는 %s살이고 %scm입니다." %(27,177))
print("부산 가는 길은 {2}와 {0} 그리고 {1}가 있습니다.".format("KTX","배","버스"))

height=177
place="바다"
print(f"나는 {height}cm이며, {place}에 가기를 좋아합니다.")

#탈출 문자열
print("가나다라마바사아\n자차카타파하")
print("오늘 \"스타벅스\" 갔다왔어.")
print("C:\\Users\\조근형\\Desktop\\Python Workspace")
print("남산위에 백두산이\r동해물과")
print("동해물과과\b백두산이")'''

# metro=["정준하", "유재석", "하하", "조세호"]
# metro.append("노홍철")
# metro.insert(1, "정형돈")
# metro.append("정준하")
# print(metro)
# print(metro.count("정준하"))

# x_list = [2,3,5,6,8]
# x_list.sort()
# print(x_list)
# x_list.clear()
# print(x_list)
y_list=("조세호", 25, False)
print(y_list)
x_list = [2,3,5,6,8]
x_list.extend(y_list)
print(x_list)