fileWriter = open("deneme.txt", mode="a")
#fileWriter.write("\ntest")
fileWriter.close()
fileReader = open("deneme.txt", mode="r")
lines = fileReader.readlines()
#for i in lines:
     #print(i)
#fileReader.close()

with open("deneme.txt", mode="r") as dosya:
    print(dosya.seek(10))
    print(dosya.read(20))

with open("deneme.txt", mode="r+") as dosya:
    data = dosya.readlines()
    data.insert(1,"test\n")
    dosya.seek(0)
    dosya.writelines(data)