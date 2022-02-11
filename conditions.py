nickname = "cenk"
password = "123"

name = input("name\n")
pss = input("password\n")

if((nickname == name) and  (pss == password)):
    print("kullanıcı adı ve parola doğru")
elif((nickname == name) and  (pss != password)):
    print("parola yanlış")
elif((nickname != name) and  (pss == password)):
    print("nickname yanlış")
else:
    print("kullanıcı adı ve parola yanlış")