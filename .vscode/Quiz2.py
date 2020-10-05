site = "http://www.youtube.com"
site1 = site.replace("http://www.", "")
site1 = site1[:site1.index(".")]
code = site1[:3] + str(len(site1)) + str(site1.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(site1, code))
w=site1
s=code
print(f"{w}의 비밀번호는 {s}입니다.")