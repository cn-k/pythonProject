name = "cenk"
pss = "123"

while(True):
    nickname = input("nickname: \n")
    password = input("password: \n")
    if((nickname==name) and (password==pss)):
        print("login")
        break;
    print("kullanıcı adı veya parola yanlış")
